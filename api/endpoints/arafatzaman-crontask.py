from middlewares import enableCORS
import requests
import time
from flask import jsonify, Response
from api.index import Endpoint

## Ping the remix dev site
BASE = "https://arafatzaman.dev"
PAGES: dict[str, str] = {
    "HOME": "/",
    "PORTFOLIO": "/portfolio/",
    "PROJECTS": "/projects/",
    "BLOG": "/blog/",
    "CONTACT": "/contact/"
}

@enableCORS
def remixDev() -> tuple[Response, int]:
    """
    A cron task to ping each route of the remix server
    """
    status_codes: dict[str, int] = {}
    code = 400
    for page in PAGES:
        stamp = time.time()
        resp = requests.get(f"{BASE}{PAGES[page]}?stamp={stamp}")
        code = resp.status_code
        status_codes[page] = resp.status_code

    return jsonify({
        "status": code,
        "pages": status_codes
    }), code

# Register the endpoint to the app
app = Endpoint("arafatzaman-ping/")
app.register(remixDev)