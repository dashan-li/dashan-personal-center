#!/bin/bash
pip install -r requirements.txt
python manage.py collectstatic --noinput --settings=personal_center.settings.prod
python manage.py migrate --settings=personal_center.settings.prod
