# jsonbourne

<img src="_data/dgpy_logo.svg" alt="drawing" width="120"/> **Dynamic Graphics Python**

[![Wheel](https://img.shields.io/pypi/wheel/jsonbourne.svg)](https://img.shields.io/pypi/wheel/jsonbourne.svg)
[![Version](https://img.shields.io/pypi/v/jsonbourne.svg)](https://img.shields.io/pypi/v/jsonbourne.svg)
[![py_versions](https://img.shields.io/pypi/pyversions/jsonbourne.svg)](https://img.shields.io/pypi/pyversions/jsonbourne.svg)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

**Install:** `pip install jsonbourne`

```python
from jsonbourne import json
string = json.dumps({"a":1, "b":2, "c":3})  # '{"a": 1, "b": 2, "c": 3}'
```

**`jsonbourne` finds the best json it can!** On import `jsonbourne` gets to
work spying on your python env. `jsonbourne`, the most highly qualified json-CIA-agent, will import the best
python-json library it can find; if `jsonbourne`'s cover is blown (meaning: the
only json library found is the python stdlib json), `jsonbourne` will fallback
to
the python stdlib json.

`jsonbourne` will look for the following json-packages in the following order:

  1) `rapidjson`
  2) `orjson`
  3) `ujson`
  4) `simplejson`

## Custom lib preferences

```python
from jsonbourne import import_json
json = import_json(("ujson", "rapidjson"))  # prefer ujson then rapidjson
string = json.dumps({"a":1, "b":2, "c":3})  # '{"a": 1, "b": 2, "c": 3}'
```

## Installing better JSONS:

  1) `rapidjson`
      - `pip install python-rapidjson` [pip]
      - `conda install -c anaconda python-rapidjson` [conda anaconda/defaults]
      - `conda install -c conda-forge python-rapidjson` [conda-forge]
  2) `orjson`
      - `pip install orjson` [pip]
  3) `ujson` *(ujson prefers conda over pip)*
      - `pip install ujson` [pip]
      - `conda install -c anaconda ujson` [conda anaconda/defaults]
      - `conda install -c conda-forge ujson` [conda-forge]
  4) `simplejson`
      - `pip install simplejson` [pip]
      - `conda install -c anaconda simplejson` [conda anaconda/defaults]
      - `conda install -c conda-forge simplejson` [conda-forge]
