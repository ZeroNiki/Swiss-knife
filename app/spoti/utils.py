import re

def spoti_url_validation(url):
    spoti_regex =  re.compile(r'https://open\.spotify\.com/track/\S*')    
    spoti_regex_match = re.match(spoti_regex, url)
    
    if spoti_regex_match:
        return spoti_regex_match

    return spoti_regex_match
