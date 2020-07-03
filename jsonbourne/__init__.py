# -*- coding: utf-8 -*-
"""`jsonbourne` finds the best python-json-lib for the job

Dynamic Graphics Python
"""

from jsonbourne import json
from jsonbourne.core import JSON
from jsonbourne.core import JsonDict
from jsonbourne.core import JsonObj
from jsonbourne.core import JsonObjMutableMapping

VERSION_MAJOR = 0
VERSION_MINOR = 2
VERSION_PATCH = 0
VERSION_INFO = (VERSION_MAJOR, VERSION_MINOR, VERSION_PATCH)
__version__ = f"{VERSION_MAJOR}.{VERSION_MINOR}.{VERSION_PATCH}"

JSONLIB = json.__name__

import_json = json.import_json
__all__ = [
    "VERSION_MAJOR",
    "VERSION_MINOR",
    "VERSION_PATCH",
    "VERSION_INFO",
    "__version__",
    "JsonObjMutableMapping",
    "JsonObj",
    "JsonDict",
    "JSON",  # js/ts JSON
    "json",  # json compat lib
]
