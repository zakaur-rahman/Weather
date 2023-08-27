#!/usr/bin/env sh

set -o errexit
pip3 install -r requirements.txt

python manage.py collectstatic
python3 manage.py migrate