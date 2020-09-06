from __future__ import unicode_literals
import flask
from flask import render_template, request, jsonify, send_from_directory
import youtube_dl
from flask_cors import CORS
import re

app = flask.Flask(__name__, static_url_path='')
CORS(app, supports_credentials=True)
app.config["DEBUG"] = True
app.config['SECRET_KEY'] = 'secret!'
app.config['CORS_HEADERS'] = 'Content-Type'
youtubeUrlRegx = re.compile('^(https?\:\/\/)?(www\.)?(youtube\.com|youtu\.?be)\/.+$')

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
        "message": "Not a valid Youtube URL"
    }
    if (isValidUrl(request.args.get('video'))):
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                response = ydl.extract_info(request.args.get('video'), False)
    return jsonify(response)

@app.route('/download', methods=['GET'])
def download():
    response = {'message': 'Download Completed'}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        response = ydl.download([request.args.get('video')])
    return jsonify(response)

def isValidUrl(url):
    return re.match(youtubeUrlRegx, url) is not None

# app.run()

if __name__ == '__main__':
    app.run()
