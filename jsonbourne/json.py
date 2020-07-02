# -*- coding: utf-8 -*-
from jsonbourne.jsonlib.base import JsonLib


def _import_rapidjson():
    from jsonbourne.jsonlib._rapidjson import RAPIDJSON

    return RAPIDJSON


def _import_orjson():
    from jsonbourne.jsonlib._orjson import ORJSON

    return ORJSON


def _import_json_stdlib():
    from jsonbourne.jsonlib._json_stdlib import JSON_STDLIB

    return JSON_STDLIB


def import_json(jsonlibs=["orjson", "rapidjson"]) -> JsonLib:
    lib2funk = {
        "rapidjson": _import_rapidjson,
        "orjson": _import_orjson,
    }

    for mod in jsonlibs:
        try:
            return lib2funk[mod]()
        except ImportError:
            pass

    return _import_json_stdlib()


_json = import_json()
loads = _json.loads
dumps = _json.dumps
dumpb = _json.dumpb
