# A fun flask API
> This is just a fun little flask API I made where random endpoints can be accessed to do cool stuffs.

---
### How to add an endpoint?

I have streamlined the process of adding an endpoint so that it is really simple to do so. Here is how you can add your own endpoint:

1. Navigate to /api/endpoints folder. 
2. Create a .py file with your endpoint
3. Write the following code

```python
from flask import jsonify
from api.index import Endpoint

def myEndpoint():
    ''' This is a normal flask endpoint '''
    # Edit however your want
    return jsonify({"test": "success"})

Route = Endpoint("/barplot") # The path parameter is just a flask parameter, can be edited however you want.
Route.register(myEndpoint)

```

4. And that is it!