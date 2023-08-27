#!/usr/bin/env sh

venv\Scripts\activate

set -o errexit
pip3 install -r requirements.txt

python3 manage.py collectstatic
python3 manage.py collectstatic --no-input
python3 manage.py migrate