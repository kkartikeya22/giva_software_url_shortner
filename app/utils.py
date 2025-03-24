import hashlib

def generate_short_code(url: str) -> str:
    """Generates a unique short code for a given URL."""
    return hashlib.md5(url.encode()).hexdigest()[:6]
