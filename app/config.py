from dotenv import load_dotenv
import os

load_dotenv()

SECRET = str(os.getenv("SECRET"))
