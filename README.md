# jsonbourne

<img src="https://github.com/dynamic-graphics-inc/dgimages/blob/master/dgpy/dgpy_logo.svg?raw=true" alt="drawing" width="120"/> **Dynamic Graphics Python**

[![Wheel](https://img.shields.io/pypi/wheel/jsonbourne.svg)](https://img.shields.io/pypi/wheel/jsonbourne.svg)
[![Version](https://img.shields.io/pypi/v/jsonbourne.svg)](https://img.shields.io/pypi/v/jsonbourne.svg)
[![py_versions](https://img.shields.io/pypi/pyversions/jsonbourne.svg)](https://img.shields.io/pypi/pyversions/jsonbourne.svg)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

**Install:** `pip install jsonbourne`

```python
from jsonbourne import json
string = json.dumps({"a":1, "b":2, "c":3})  # '{"a": 1, "b": 2, "c": 3}'
```

**`jsonbourne` finds the best json-lib (python-rapidjson/orjson) it can!** On import `jsonbourne` gets to
work spying on your python env. `jsonbourne`, the most highly qualified json-CIA-agent, will import the best
python-json library it can find; if `jsonbourne`'s cover is blown (meaning: the
only json library found is the python stdlib json), `jsonbourne` will fallback
to
the python stdlib json.

`jsonbourne` will look for the following json-packages in the following order:

  1) `rapidjson`
  2) `orjson`

## Custom lib preferences

```python
from jsonbourne import _import_json
json = _import_json(("ujson", "rapidjson"))  # prefer ujson then rapidjson
string = json.dumps({"a":1, "b":2, "c":3})  # '{"a": 1, "b": 2, "c": 3}'
```

## Installing better JSON lib:

  1) `rapidjson`
      - `pip install python-rapidjson` [pip]
      - `conda install -c anaconda python-rapidjson` [conda anaconda/defaults]
      - `conda install -c conda-forge python-rapidjson` [conda-forge]
  2) `orjson`
      - `pip install orjson` [pip]
