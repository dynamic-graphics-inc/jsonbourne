# -*- coding: utf-8 -*-
from typing import Any

from jsonbourne.jsonlib.base import JsonLib
from jsonbourne.jsonlib.base import _json_encode_default

try:
    import orjson
except ImportError:
    orjson = None

try:
    import numpy as np
except ImportError:
    np = None


class ORJSON(JsonLib):
    @staticmethod
    def dumps(
        data: Any, pretty: bool = False, sort_keys: bool = False, default=None, **kwargs
    ) -> str:
        return ORJSON.dumpb(
            data, pretty=pretty, sort_keys=sort_keys, default=default, **kwargs
        ).decode(encoding="utf-8")

    @staticmethod
    def dumpb(
        data: Any, pretty: bool = False, sort_keys: bool = False, default=None, **kwargs
    ) -> bytes:
        option = 0
        if pretty:
            option |= orjson.OPT_INDENT_2
        if sort_keys:
            option |= orjson.OPT_SORT_KEYS
        if np:
            option |= orjson.OPT_SERIALIZE_NUMPY

        return orjson.dumps(
            data, option=option, default=default or _json_encode_default, **kwargs
        )

    @staticmethod
    def loads(string: str, **kwargs) -> Any:
        return orjson.loads(string, **kwargs)


if __name__ == "__main__":
    pass
