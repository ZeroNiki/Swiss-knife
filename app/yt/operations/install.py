import yt_dlp as ytd
import os


current_script_path = os.path.dirname(os.path.abspath(__file__))
relative_path = os.path.join(current_script_path, '..', '..', 'media') 
BASE_DIR = os.path.abspath(relative_path)

def dw1080(link):
    options = {
        'skip-download': True,
        'format_sort': ['res:1080', 'ext:mp4:m4a'],
        'outtmpl': f'{BASE_DIR}/%(title)s.%(ext)s'
    }

    with ytd.YoutubeDL(options) as ytdl:
        ytdl.download([link])
        result = ytdl.extract_info("{}".format(link))
        title = ytdl.prepare_filename(result)

    return title 


def dw720(link):
    options = {
        'skip-download': True,
        'format_sort': ['res:720', 'ext:mp4:m4a'],
        'outtmpl': f'{BASE_DIR}/%(title)s.%(ext)s'
    }

    with ytd.YoutubeDL(options) as ytdl:
        ytdl.download([link])
        result = ytdl.extract_info("{}".format(link))
        title = ytdl.prepare_filename(result)

    return title 



def dw360(link):
    options = {
        'skip-download': True,
        'format_sort': ['res:360', 'ext:mp4:m4a'],
        'outtmpl': f'{BASE_DIR}/%(title)s.%(ext)s'
    }

    with ytd.YoutubeDL(options) as ytdl:
        ytdl.download([link])
        result = ytdl.extract_info("{}".format(link))
        title = ytdl.prepare_filename(result)

    return title 


def mp3(link):
    options = {
        'skip-download': True,
        'format': 'bestaudio/best',
        'outtmpl': f'{BASE_DIR}/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with ytd.YoutubeDL(options) as ytdl:
        ytdl.download([link])
        result = ytdl.extract_info("{}".format(link))
        title = ytdl.prepare_filename(result)[:-5]

    return f"{title}.mp3" 
