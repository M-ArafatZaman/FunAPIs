from flask import Blueprint
import os
import importlib.util
from typing import List, Tuple, Callable

# class for endpoints
class Endpoint:
    def __init__(self, url: str):
        self.url: str = url
        self._fn = None
    
    def register(self, fn):
        self._fn = fn

    def getFn(self):
        if self._fn != None:
            return self._fn 
        # Didnt register Fn yet
        raise NotImplementedError()

# Load endpoints
def loadEndpoints():
    '''
    This function traverses through each directories in the endpoints
    And loads and registers each endpoints
    '''
    # The api blueprint
    API_BLUEPRINT = Blueprint("api", __name__, url_prefix="/api")

    CURR_DIR = os.getcwd()
    PATH = os.path.abspath(__file__)
    SCRIPT_DIR = os.path.dirname(PATH)
    ENDPOINT_DIR_PATH = os.path.join(SCRIPT_DIR, 'endpoints')

    url_route: Tuple[str, Callable] = []
    
    # Change dir to the endpoints dir
    os.chdir(ENDPOINT_DIR_PATH)
    # Iterate through each files
    for path in os.listdir():
        mod_path = os.path.join(os.getcwd(), path)
        # Import file if it is a valid python file
        if os.path.isfile(mod_path) and path.endswith(".py"):
            spec = importlib.util.spec_from_file_location(path, mod_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            for _globals in getGlobalsFromModule(module.__dir__()):
                # Load
                _G = getattr(module, _globals)
                if isinstance(_G, Endpoint):
                    # Add to url patterns
                    url_route.append((_G.url, _G.getFn()))

    # Change back to the curr dir
    os.chdir(CURR_DIR)

    # Register routes
    for pathName, fn in url_route:
        API_BLUEPRINT.route(pathName)(fn)

    return API_BLUEPRINT
            
# Util functions
def getGlobalsFromModule(dir: List[str]):
    _globals = []
    for i in dir:
        if i.startswith("__") and i.endswith("__"):
            continue
        _globals.append(i)
    return _globals