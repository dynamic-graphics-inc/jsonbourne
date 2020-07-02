# -*- coding: utf-8 -*-
from typing import Any

import rapidjson

from jsonbourne.jsonlib.base import JsonLib
from jsonbourne.jsonlib.base import _json_encode_default

JSONLIB = 'rapidjson'


class RAPIDJSON(JsonLib):
    @staticmethod
    def dumps(
        data: Any, pretty: bool = False, sort_keys: bool = False, default=None, **kwargs
    ) -> str:
        return rapidjson.dumps(
            data,
            indent=2 if pretty else None,
            sort_keys=sort_keys,
            default=default or _json_encode_default,
            datetime_mode=rapidjson.DM_ISO8601,
            **kwargs,
        )

    @staticmethod
    def dumpb(
        data: Any, pretty: bool = False, sort_keys: bool = False, default=None, **kwargs
    ) -> str:
        return RAPIDJSON.dumps(
            data, pretty=pretty, sort_keys=sort_keys, default=default, **kwargs
        ).encode()

    @staticmethod
    def loads(string: str, **kwargs) -> Any:
        return rapidjson.loads(string, **kwargs)


JSONEncoder = rapidjson.Encoder
JSONDecoder = rapidjson.Decoder
JSONDecodeError = rapidjson.JSONDecodeError

if __name__ == "__main__":
    pass
    # from doctest import testmod
    # testmod()
