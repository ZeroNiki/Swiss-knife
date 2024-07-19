import os
from dotenv import load_dotenv

load_dotenv()

current_script_path = os.path.dirname(os.path.abspath(__file__))
relative_path = os.path.join(current_script_path, '..', '..', 'media') 
FULL_DIR = os.path.abspath(relative_path) + "/"
YT_LINK = "https://yt.artemislena.eu/search?q="
GENIUS_API = os.getenv("GENIUS_API")
DRIVER = os.getenv("DRIVER")

