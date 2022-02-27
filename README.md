# almostapt-api

An FastAPI based API for my AlmostAPT project identifying uncategorized, or threat groups without an official vendor identifier.

## Requirements

- Python 3.9+

## Installation

```bash
$ pip install poetry
$ poetry install

$ hypercorn main:app --reload
INFO: Running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

## Usage

```bash
curl localhost:8000/api/v1/{groupname}

curl localhost:8000/api/v1/TAG22

curl localhost:8000/api/v1/all  >> returns all 30+ database entries

```
