from pymongo import MongoClient
from app.config import MONGO_URI

client = MongoClient(MONGO_URI)
db = client.url_shortener
collection = db.urls

# Ensure indexes for fast lookups
collection.create_index("short_code", unique=True)
collection.create_index("long_url", unique=True)
