from os import path

from jsonbourne import __version__
from jsonbourne import import_json


def _get_version() -> str:
    _dirpath = path.split(path.realpath(__file__))[0]
    version = "UNKNOWN???"
    for i in range(3):
        _filepath = path.join(_dirpath, "pyproject.toml")
        if path.exists(_filepath):
            version = (
                [l for l in open(_filepath).read().split("\n") if "version" in l][0]
                .replace("version = ", "")
                .strip('"')
            )
            return version
        _dirpath = path.split(_dirpath)[0]
    return version


def test_version():
    assert __version__ == _get_version()


def test_uno():
    from jsonbourne import json

    dictionary = {"a": 1, "b": 2, "c": 3}
    string = json.dumps(dictionary)
    assert dictionary == json.loads(string)


def test_rapidjson():
    libname = "rapidjson"
    _rapidjson = import_json((libname,))
    dictionary = {"a": 1, "b": 2, "c": 3}
    string = _rapidjson.dumps(dictionary)
    assert dictionary == _rapidjson.loads(string)
    assert _rapidjson.__name__ == libname


def test_ujson():
    libname = "ujson"
    _ujson = import_json((libname,))
    dictionary = {"a": 1, "b": 2, "c": 3}
    string = _ujson.dumps(dictionary)
    assert dictionary == _ujson.loads(string)
    assert _ujson.__name__ == libname


def test_orjson():
    libname = "orjson"
    _orjson = import_json((libname,))
    dictionary = {"a": 1, "b": 2, "c": 3}
    string = _orjson.dumps(dictionary)
    assert dictionary == _orjson.loads(string)
    assert _orjson.__name__ == libname


def test_simplejson():
    libname = "simplejson"
    _simplejson = import_json((libname,))
    dictionary = {"a": 1, "b": 2, "c": 3}
    string = _simplejson.dumps(dictionary)
    assert dictionary == _simplejson.loads(string)
    assert _simplejson.__name__ == libname


def test_stdlibjson():
    libname = "json"
    _stdlibjson = import_json((libname,))
    dictionary = {"a": 1, "b": 2, "c": 3}
    string = _stdlibjson.dumps(dictionary)
    assert dictionary == _stdlibjson.loads(string)
    assert _stdlibjson.__name__ == libname
