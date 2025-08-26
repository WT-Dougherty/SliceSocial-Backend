# SliceBackend
Server-side logic for Slice Social

## Setup Virtual Environment
```bash
# activate virtual environment
$ source .venv/bin/activate

# establish virtual environment
$ /opt/homebrew/opt/python@3.13/bin/python3.13 -m venv /Users/willdougherty/Dev/GitHub/SliceBackend/.venv

# checks: ensure that the venv is selected for package management & upgrade pip
$ which python3
$ python3 -m pip install --upgrade pip

# install required packages
$ pip install -r requirements.txt

# run the server
$ fastapi dev main.py

# when done working, update requirements.txt to show any new packages
$ pip freeze > requirements.txt
```