import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
BASE_URL = os.getenv("BASE_URL", "http://localhost:8000")
