import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
BASE_URL = "https://giva-software-url-shortner-updated.onrender.com/"
