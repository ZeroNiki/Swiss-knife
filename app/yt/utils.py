import re

def youtube_url_validation(url):
    youtube_regex = re.compile(r"http(?:s?):\/\/(?:www\.)?youtu(?:be\.com\/watch\?v=|\.be\/)([\w\-\_]*)(&(amp;)?‌​[\w\?‌​=]*)?")
    youtube_regex_match = re.match(youtube_regex, url)
    
    if youtube_regex_match:
        return youtube_regex_match

    return youtube_regex_match
