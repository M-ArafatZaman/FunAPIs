import matplotlib
matplotlib.use("Agg")
'''
This switches the backend engine because the default engine uses tkinter or something idk.
Prevents Warning: 
UserWarning: Starting a Matplotlib GUI outside of the main thread will likely fail.
'''
from flask import jsonify, request, send_file
from api.index import Endpoint
import matplotlib.pyplot as plt
from typing import List
import io

def barplot():
    data = request.args.get("data")
    
    # If data does not exists, return a bad request response
    if not data:
        return jsonify({
            "status": 400,
            "message": "Missing required 'data' GET parameter."
        }), 400
    
    try:
        # Form data
        y: List[str] = data.split(",")
        y: List[float] = [float(i) for i in y]
        x: List[int] = [i+1 for i in range(len(y))]

        # Plot data
        plt.bar(x, y, label="Numbers visualized") 
        plt.legend(loc="upper right")
        fig = plt.gcf()

        # Create file buffer
        buffer = io.BytesIO()
        fig.savefig(buffer, format="png")
        buffer.seek(0)
        fig.clear()
        plt.close()

        response = send_file(buffer, mimetype="image/png")
        #buffer.close()

        return response

    except Exception:
        
        return jsonify({"status": 500, "message": "A server error occured."}), 500


BarPlotEndpoint = Endpoint("/barplot/")
BarPlotEndpoint.register(barplot)
