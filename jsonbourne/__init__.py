# -*- coding: utf-8 -*-
"""`jsonbourne` finds the best python-json-lib for the job

Dynamic Graphics Python
"""

from jsonbourne._json import JSON, JsonObj, JsonDict


VERSION_MAJOR = 0
VERSION_MINOR = 1
VERSION_PATCH = 1
VERSION_INFO = (VERSION_MAJOR, VERSION_MINOR, VERSION_PATCH)
__version__ = f"{VERSION_MAJOR}.{VERSION_MINOR}.{VERSION_PATCH}"

JSONS = ("rapidjson", "orjson", "ujson", "simplejson")
JSONLIB = None


def import_json(jsons=JSONS):
    """Import the best possible given a priority list"""
    for mod in jsons:
        try:
            return __import__(mod)
        except ImportError:
            pass
    import json as _json

    return _json


json = import_json()
JSONLIB = json.__name__

__all__ = [
    "JsonObj",
    "JsonDict",
    "JSON",
    "VERSION_MAJOR",
    "VERSION_MINOR",
    "VERSION_PATCH",
    "VERSION_INFO",
    "__version__",
]
