# jsonbourne

`pip install jsonbourne`

`jsonbourne` finds the best json it can.

```python
from jsonbourne import json
string = json.dumps({"a":1, "b":2, "c":3})  # '{"a": 1, "b": 2, "c": 3}'
```

On import `jsonbourne` gets to work spying on your python env.
`jsonbourne`, the most highly qualified json-CIA-agent, will import the best
python-json library it can find; if `jsonbourne`'s cover is blown (meaning: the only
json library found is the python stdlib json), `jsonbourne` will fallback to
the python stdlib json.

`jsonbourne` will look for the following json-packages in the following order:

  1) `rapidjson` (`pip install python-rapidjson` || `conda install -c anaconda python-rapidjson` || `conda install -c conda-forge python-rapidjson`)
  2) `orjson` (`pip install orjson`)
  3) `ujson` (`pip install ujson` || `conda install ujson`)
  4) `simplejson` (`pip install simplejson` || `conda install ujson`)

## Installing the JSONS

  1) `rapidjson`
    - `pip install python-rapidjson` [pip]
    - `conda install -c anaconda python-rapidjson` [conda anaconda/defaults]
    - `conda install -c conda-forge python-rapidjson` [conda-forge]
  2) `orjson`
    - `pip install orjson` [pip]
  3) `ujson`
    - `pip install ujson` [pip]
    - `conda install -c anaconda ujson` [conda anaconda/defaults]
    - `conda install -c conda-forge ujson` [conda-forge]
  4) `simplejson`
    - `pip install simplejson` [pip]
    - `conda install -c anaconda simplejson` [conda anaconda/defaults]
    - `conda install -c conda-forge simplejson` [conda-forge]

