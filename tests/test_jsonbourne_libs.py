import datetime

import pytest

try:
    from jsonbourne.jsonlib._json_stdlib import JSON_STDLIB
    from jsonbourne.jsonlib._orjson import ORJSON
    from jsonbourne.jsonlib._rapidjson import RAPIDJSON
except (ImportError, ModuleNotFoundError):
    pass

pytestmark = [pytest.mark.jsonlibs, pytest.mark.optdeps]

D = {
    "key": "value",
    "list": [1, 2, 3, 4, 5],
    "dt": datetime.datetime(1970, 1, 1, 0, 0, 0, 1),
    "sub": {'b': 3, 'key': 'val', 'a': 1,},
}


def test_basic():
    rj = RAPIDJSON.dumps(D)
    oj = ORJSON.dumps(D)
    sj = JSON_STDLIB.dumps(D)
    a = [rj, oj, sj]
    assert len(set(a)) == 1


def test_pretty():
    rj = RAPIDJSON.dumps(D, pretty=True)
    oj = ORJSON.dumps(D, pretty=True)
    sj = JSON_STDLIB.dumps(D, pretty=True)
    a = [rj, oj, sj]
    assert len(set(a)) == 1


def test_sort_keys():
    rj = RAPIDJSON.dumps(D, sort_keys=True)
    oj = ORJSON.dumps(D, sort_keys=True)
    sj = JSON_STDLIB.dumps(D, sort_keys=True)
    a = [rj, oj, sj]
    assert len(set(a)) == 1


def test_pretty_sort_keys():
    rj = RAPIDJSON.dumps(D, pretty=True, sort_keys=True)
    oj = ORJSON.dumps(D, pretty=True, sort_keys=True)
    sj = JSON_STDLIB.dumps(D, pretty=True, sort_keys=True)
    a = [rj, oj, sj]
    assert len(set(a)) == 1


def test_datetime():
    data = {
        "dt": datetime.datetime(1970, 1, 1, 0, 0, 0, 1),
    }
    rj = RAPIDJSON.dumps(data)
    oj = ORJSON.dumps(data)
    sj = JSON_STDLIB.dumps(data)
    a = [rj, oj, sj]
    assert len(set(a)) == 1
