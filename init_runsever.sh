#! /bin/bash

python3 manage.py collectstatic
python3 manage.py migrate

sudo service nginx start

gunicorn --bind unix:/tmp/127.0.0.1.socket drf_vue_blog.wsgi:application

