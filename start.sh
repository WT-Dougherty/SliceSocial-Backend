#!/bin/bash

ls
echo "starting virtual environment"
source .venv/bin/activate
echo

echo "current interpreter executable"
which python3
echo

echo "configuring environment"
python3 -m pip install --upgrade pip
pip install -r requirements.txt
echo

echo "starting server"
fastapi dev main.py

echo "environment is ready"