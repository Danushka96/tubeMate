![deploy](https://github.com/Danushka96/tubeMate/workflows/deploy/badge.svg?branch=master)

# TubeMate

Download Videos to your local storage from sites listed here.

[https://ytdl-org.github.io/youtube-dl/supportedsites.html](https://ytdl-org.github.io/youtube-dl/supportedsites.html)

## Demo
[http://tubematelk.ml/](http://tubematelk.ml/)

![](https://i.imgur.com/iuzgWpe.png)


## How to setup

### Requirements
* [pip3](https://bootstrap.pypa.io/get-pip.py)
* [node 10.x](https://nodejs.org/dist/latest-v10.x/)

### Installation

1. Clone the project
2. `pip install requirements.txt`
3. `node install`
4. `python tubemate.py`
5. `npm serve`

### Install with Docker

* `docker pull docker.pkg.github.com/danushka96/tubemate/tubemate:latest`
* `docker run --name tubemate -p 5000:5000 docker.pkg.github.com/danushka96/tubemate/tubemate:latest`
