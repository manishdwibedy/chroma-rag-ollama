#!/bin/bash
# Create and activate a Python virtual environment, then install dependencies

python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
