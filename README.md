# sample-django-on-docker

1. Quick installation

    mkdir hellpo && cd hello
    pipenv install django==3.1.0
    pipenv shell
    django-admin startproject config .
    python manage.py migrate
    python manage.py runserver