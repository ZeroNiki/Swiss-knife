from .yandex import get_yandex_track
from .yt import yt_search
from .dw import download_music, downlad_cover
from .lyrics import get_lyric
from .mtd_mp3 import change_cover, change_metadata

from .config import FULL_DIR


def main(url):
    global link
    results = get_yandex_track(url)

    author = results[0]
    clear_author = author.replace('&', '')

    track_name = results[1]
    cover_url = results[2]

    keyword = clear_author + " " + track_name
    file_name = f'{clear_author} {track_name}.mp3'
    cover_name = f'{clear_author} {track_name}.jpg'

    link = yt_search(keyword) 

    download_music(link, clear_author, track_name)
    downlad_cover(clear_author, track_name, FULL_DIR + "/", cover_url)

    lyric = get_lyric(track_name, clear_author)

    change_metadata(f"{FULL_DIR}/{file_name}", clear_author, track_name, lyric)
    change_cover(f"{FULL_DIR}/{file_name}", f"{FULL_DIR}{cover_name}")

    return f"{FULL_DIR}{file_name}"
    
