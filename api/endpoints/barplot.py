from flask import jsonify
from api.index import Endpoint

def barplot():
    return jsonify({"test": "success"})

BarPlotEndpoint = Endpoint("/barplot")
BarPlotEndpoint.register(barplot)

def barplot2():
    return jsonify({"test": "WOW FROM THE SECOND"})

BPE2 = Endpoint("/bp2")
BPE2.register(barplot2)