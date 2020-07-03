# -*- coding: utf-8 -*-
from jsonbourne._import import import_json
from jsonbourne.jsonlib.base import JsonLib

_json = import_json()
loads = _json.loads
dumps = _json.dumps
dumpb = _json.dumpb
