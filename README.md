# Python package index services

A list of managed Python package index services

## Local

### Environment set-up

```shell
pip install -r requirements.txt
```

### Building

```shell
sphinx-build -b html src build
```

### Serving

Any static file server will do, but you likely already have Python installed:

```shell
python -m http.server -d build
```
