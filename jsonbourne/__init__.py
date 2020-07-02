# -*- coding: utf-8 -*-
"""`jsonbourne` finds the best python-json-lib for the job

Dynamic Graphics Python
"""

from jsonbourne import json
from jsonbourne.main import JSON
from jsonbourne.main import JsonDict
from jsonbourne.main import JsonObj
from jsonbourne.main import JsonObjMutableMapping

VERSION_MAJOR = 0
VERSION_MINOR = 1
VERSION_PATCH = 1
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
    "JsonObj",
    "JsonDict",
    "JSON",
    "JsonObjMutableMapping",
    "import_json",
]
