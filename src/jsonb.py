# -*- coding: utf-8 -*-
"""`jsonbourne` finds the best python-json-lib for the job

Dynamic Graphics Python
"""

from jsonbourne import json
from jsonbourne._import import import_json
from jsonbourne._version import VERSION_INFO
from jsonbourne._version import VERSION_MAJOR
from jsonbourne._version import VERSION_MINOR
from jsonbourne._version import VERSION_PATCH
from jsonbourne._version import __version__
from jsonbourne.core import JSON
from jsonbourne.core import JsonDict
from jsonbourne.core import JsonObj
from jsonbourne.core import JsonObjMutableMapping
from jsonbourne.core import parse
from jsonbourne.core import stringify

JSONLIB = json.__name__

__all__ = [
    "JSON",  # js/ts JSON (THE ONE TO USE)
    "json",  # json compat lib
    # core
    "JsonObjMutableMapping",
    "JsonObj",
    "JsonDict",
    # import
    "import_json",
    # util funks
    "stringify",
    "parse",
    # Version stuff
    "VERSION_MAJOR",
    "VERSION_MINOR",
    "VERSION_PATCH",
    "VERSION_INFO",
    "__version__",
]
