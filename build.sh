#!/usr/bin/env bash
# roda no Render a cada deploy (Build Command: bash build.sh)
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
