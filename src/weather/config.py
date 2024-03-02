import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

API_KEY = os.environ.get("WEATHER_API")
BASE_URL = os.environ.get("BASE_URL")