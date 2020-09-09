from __future__ import unicode_literals
import flask
from flask import render_template, request, jsonify, send_from_directory
import youtube_dl
from flask_cors import CORS
import re

app = flask.Flask(__name__, static_url_path='')
CORS(app, supports_credentials=True)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'secret!'
app.config['CORS_HEADERS'] = 'Content-Type'
urlRegx = re.compile('^(http|https|ftp)\://([a-zA-Z0-9\.\-]+(\:[a-zA-Z0-9\.&amp;%\$\-]+)*@)*((25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[1-9])\.(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[1-9]|0)\.(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[1-9]|0)\.(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[0-9])|localhost|([a-zA-Z0-9\-]+\.)*[a-zA-Z0-9\-]+\.(com|edu|gov|int|mil|net|org|biz|arpa|info|name|pro|aero|coop|museum|[a-zA-Z]{2}))(\:[0-9]+)*(/($|[a-zA-Z0-9\.\,\?\'\\\+&amp;%\$#\=~_\-]+))*$')

class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    # emit('my_response', d, namespace='/test')
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('templates/js', path)

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('templates/css', path)

@app.route('/img/<path:path>')
def send_img(path):
    return send_from_directory('templates/img', path)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/info', methods=['GET'])
def info():
    response = {
        "error": "400",
        "message": "Not a valid URL"
    }
    if (isValidUrl(request.args.get('video'))):
        try:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    response = ydl.extract_info(request.args.get('video'), False)
        except:
            print("Not a Valid URL")
    return jsonify(response)

@app.route('/download', methods=['GET'])
def download():
    response = {'message': 'Download Completed'}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        response = ydl.download([request.args.get('video')])
    return jsonify(response)

def isValidUrl(url):
    return re.match(urlRegx, url) is not None

# app.run()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
