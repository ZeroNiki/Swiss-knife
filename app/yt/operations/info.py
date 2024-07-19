import yt_dlp as ytd

def getinfo(link):
    with ytd.YoutubeDL() as ydl: 
        info_dict = ydl.extract_info(link, download=False)
        video_url = info_dict.get("url", None)
        video_id = info_dict.get("id", None)
        video_title = info_dict.get('title', None)
        return [video_title, video_id, link]
    
