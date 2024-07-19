import json
from lyricsgenius import Genius

from .config import GENIUS_API
from .config import FULL_DIR

def get_lyric(trackName: str, authorName: str):
    try:
        genius = Genius(GENIUS_API)
        song_name = genius.search_song(trackName, authorName)
        song_name.save_lyrics('lyric.json')

        with open(f'lyric.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

        lyrics = data.get('lyrics')

        return lyrics
    except AttributeError:
        print("No luric")
        return "No luric"
