import os
from .path import PATH_PROGRAM
from src.utils.functions import json_decode

PATHFILE = f"{ PATH_PROGRAM }/package.json"
package = json_decode(PATHFILE)