import re

def yand_url_validation(url):
    yand_regex = re.compile(r'https://music\.yandex\.ru/album/\d+/track/\d+(\?\S*)?')
    yand_regex_match = re.match(yand_regex, url)
    
    if yand_regex_match:
        return yand_regex_match

    return yand_regex_match
