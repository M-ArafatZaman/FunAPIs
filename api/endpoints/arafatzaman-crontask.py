from middlewares import enableCORS
import requests
import time
from flask import jsonify, Response
from api.index import Endpoint

## Ping the remix dev site

ARAFATZAMAN = "https://arafatzaman.dev/"

@enableCORS
def remixDev() -> tuple[Response, int]:
    """
    A cron task to ping the remix server
    """
    stamp = time.time()
    resp = requests.get(f"{ARAFATZAMAN}?stamp={stamp}")

    return jsonify({
        "status": resp.status_code
    }), resp.status_code

# Register the endpoint to the app
app = Endpoint("arafatzaman-ping/")
app.register(remixDev)