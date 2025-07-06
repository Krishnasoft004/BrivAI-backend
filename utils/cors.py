from flask import request
from urllib.parse import urlparse

def apply_cors_headers(response):
    origin = request.headers.get("Origin")
    if origin:
        parsed = urlparse(origin)
        if parsed.hostname and (
            parsed.hostname.endswith("vercel.app") or "localhost" in parsed.hostname
        ):
            response.headers["Access-Control-Allow-Origin"] = origin
            response.headers["Access-Control-Allow-Credentials"] = "true"
            response.headers["Access-Control-Allow-Headers"] = "Content-Type,Authorization"
            response.headers["Access-Control-Allow-Methods"] = "GET,POST,OPTIONS"
            response.headers["Vary"] = "Origin"
    return response