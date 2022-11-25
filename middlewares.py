from flask import make_response
from functools import wraps 

# Function decorator to enable cors response
def enableCORS(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Before calling

        # Call
        response = make_response( func(*args, **kwargs) )

        # After calling
        response.headers["Access-Control-Allow-Origin"] = "*"

        return response
    
    return wrapper