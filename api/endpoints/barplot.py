from flask import jsonify
from api.index import Endpoint

def barplot():
    return jsonify({"test": "success"})

BarPlotEndpoint = Endpoint("/barplot")
BarPlotEndpoint.register(barplot)
