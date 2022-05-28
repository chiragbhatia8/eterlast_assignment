# eterlast

Eterlast Assignment

To start the project simply type
    - docker-compose -f local.yml up

To create a new superuser
 - docker-compose -f local.yml run --rm django python manage.py createsuperuser

To create a new migration
 - docker-compose -f local.yml run --rm django python manage.py makemigrations

To test the API import the collection kept in the root directory with name
 `eterlast.postman_collection.json`

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)]