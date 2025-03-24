import os
import validators
import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from app.database import collection
from app.models import URLSchema
from app.utils import generate_short_code
from app.config import BASE_URL

app = FastAPI()

# Enable CORS for public access (Allow in Development, Restrict in Production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this in production to specific domains
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/shorten")
def shorten_url(url: URLSchema):
    """Shortens a given URL and supports custom aliases."""
    if not validators.url(str(url.long_url)):
        raise HTTPException(status_code=400, detail="Invalid URL")

    existing_entry = collection.find_one({"long_url": str(url.long_url)})
    if existing_entry:
        return {"short_url": f"{BASE_URL}/{existing_entry['short_code']}"}

    short_code = url.alias if url.alias else generate_short_code(str(url.long_url))

    if collection.find_one({"short_code": short_code}):
        raise HTTPException(status_code=400, detail="Custom alias already taken")

    collection.insert_one({"long_url": str(url.long_url), "short_code": short_code, "clicks": 0})
    
    return {"short_url": f"{BASE_URL}/{short_code}"}

@app.get("/{short_code}")
def redirect_to_long_url(short_code: str):
    """Redirects to the original URL from a short code."""
    entry = collection.find_one({"short_code": short_code})
    if not entry:
        raise HTTPException(status_code=404, detail="Short URL not found")

    collection.update_one({"short_code": short_code}, {"$inc": {"clicks": 1}})
    
    return RedirectResponse(entry["long_url"])

@app.get("/stats/{short_code}")
def get_url_stats(short_code: str):
    """Returns the statistics of a short URL."""
    entry = collection.find_one({"short_code": short_code}, {"_id": 0})
    if not entry:
        raise HTTPException(status_code=404, detail="Short URL not found")

    return {"long_url": entry["long_url"], "short_code": short_code, "clicks": entry["clicks"]}

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))  # Read port from environment variables
    uvicorn.run(app, host="0.0.0.0", port=port)
