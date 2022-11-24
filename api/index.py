from flask import Blueprint
import os, sys
import importlib.util
from typing import List

# class for endpoints
class Endpoint:
    def __init__(self, url: str):
        self.url: str = url
        self._fn = None

    def fn(self, *args, **kwargs):
        if self._fn != None:
            return self._fn(*args, **kwargs)
        # Must be implemented
        raise NotImplementedError()
    
    def register(self, fn):
        self._fn = fn

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
                    # Add route
                    API_BLUEPRINT.route(_G.url)(_G.fn)
                    '''
                    Equivalent to - 
                    @API_BLUEPRINT.route(url)
                    def fn():
                        pass
                    '''

    # Change back to the curr dir
    os.chdir(CURR_DIR)

    return API_BLUEPRINT
            
# Util functions
def getGlobalsFromModule(dir: List[str]):
    _globals = []
    for i in dir:
        if i.startswith("__") and i.endswith("__"):
            continue
        _globals.append(i)
    return _globals