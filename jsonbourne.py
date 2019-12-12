# -*- coding: utf-8 -*-
"""`jsonbourne` finds the best python-json-lib for the job"""

__version__ = "0.1.0"

JSONS = ("rapidjson", "orjson", "ujson", "simplejson")


def import_json(jsons=JSONS):
    """Import the best possible given a priority list"""
    for mod in jsons:
        try:
            res = __import__(mod)
            return res
        except ImportError:
            pass
    import json as _json

    return _json


json = import_json()
