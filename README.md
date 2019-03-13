# defrecord-ml

## Setup

The following should work even with a default Python 2 setup:

``` shell
pip install --upgrade virtualenv
virtualenv -p python3.6 --no-site-packages --distribute .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Testing

``` shell
.venv/bin/python3.6 -m defrecord-ml
```
