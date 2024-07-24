# SWISS-KNIFE

## About

requirements:

- django
- yt-dlp
- redis
- selenium
- bs4
- wget
- docker
- docker-compose
  etc

Django app for install youtube video(and audio), spotify music, yandex music

## Install and Start (Via Docker)

clone the repo:

```sh
git clone https://github.com/ZeroNiki/Swiss-knife.git

cd Swiss-knife
```

add your API from [Genius](https://genius.com/) and paste it in `GENIUS_API` in `.env` file:

```
GENIUS_API=apiFromGenius
```

```sh
docker-compose up --build
```

Default addres: http://0.0.0.0:8000

### If you using linux

```sh
docker-compose build

chmod +x start.sh

./start.sh
```

if you wanna close docker images:

```sh
docker stop $(docker ps -q)
```

WARNING! This command will stop all docker images. If you are running other images, use a different command

## Usage

in http://0.0.0.0:8000/ (Home page) you will see:

```
Clear cache - using for clear cache (Redis)

Youtube Download (link: http://0.0.0.0:8000/ytDownloads)
Spotify (link: http://0.0.0.0:8000/spotiDownloads)
YandexMusic (link: http://0.0.0.0:8000/yandDownloads)
```

### Youtube Download

in input paste link like this: https://www.youtube.com/watch?v=njX2bu-_Vw4
and click send (link will be stored in cache while 60s)

some time later you will download this video in 1080p, 720p, 360p, and audio(mp3)
after install you should go `home` and click `Clear cache`

### Spotify Download music

in input paste link like this: https://open.spotify.com/track/4sUTagdmyuyAxd7RvbygpQ
and click send (link will be stored in cache while 60s)

some time later will appear button `install` click it and you will start downloading the .mp3 file along with the lyrics and album cover

### Yandex Music

in input paste link like this: https://music.yandex.ru/album/2709050/track/313567
and click send (link will be stored in cache while 60s)

some time later will appear button `install` click it and you will start downloading the .mp3 file along with the lyrics and album cover
