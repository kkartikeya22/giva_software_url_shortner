# FastAPI URL Shortener

🚀 A simple and efficient URL shortener built using **FastAPI** and **MongoDB**.

## Live Demo
🔗 **Deployed at:** https://giva-software-url-shortner-updated.onrender.com

## Features
- Shorten long URLs with automatically generated short codes.
- Support for **custom aliases** (if available).
- **Redirect** short URLs to their original long URLs.
- View **click statistics** for shortened URLs.
- RESTful API with **CORS support**.

## API Endpoints
### 1️⃣ Home
**GET /**
- Displays a welcome message with API usage instructions.

### 2️⃣ Shorten URL
**POST /shorten**
- **Request Body:**
  ```json
  {
    "long_url": "https://example.com",
    "alias": "custom123"  // Optional
  }
  ```
- **Response:**
  ```json
  {
    "short_url": "https://your-domain/custom123"
  }
  ```

### 3️⃣ Redirect to Long URL
**GET /{short_code}**
- Redirects the user to the original URL.
- **Example:** Visiting `https://your-domain/custom123` redirects to `https://example.com`.

### 4️⃣ Get URL Stats
**GET /stats/{short_code}**
- Returns the number of times a short URL has been accessed.
- **Response:**
  ```json
  {
    "long_url": "https://example.com",
    "short_code": "custom123",
    "clicks": 10
  }
  ```

## Deployment
- Hosted on **Render** (or any cloud platform supporting FastAPI and MongoDB).
- Can be deployed with **Docker, Uvicorn, or Gunicorn**.

## Tech Stack
- **Backend:** FastAPI, Uvicorn
- **Database:** MongoDB
