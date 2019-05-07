#!/bin/sh
sleep 5
python3 manage.py migrate
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@localhost', 'password')" | python manage.py shell || echo 'Already have superuser'
python3 manage.py runserver