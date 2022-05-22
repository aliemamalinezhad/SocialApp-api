# Socialpy API
Hi I am Ali Emamalinezhad.
This is a simple documentation to use the project.

Tech stacks of this project:
* Django / Djago Rest Framework
* Docker
* Postgresql
* Redis
* Celery
* Swagger Api Documentation
* Pytest as a test tool
* GraphQL

1. ### Download the project:

* `git clone "https://github.com/aliemamalinezhad/socialpy-api.git"`

2. ### Build The Project:

* `docker-compose build`

3. ### Running the project:

* `docker-compose up ` \ `docker-compose up -d`

4. ### You need to create a superuser:

* `docker exec -it djago_app sh`

* `python manage.py migrate`

* `python manage.py createsuperuser`

5. ## Now you can see auto generated documentation:

* Swagger Documentation -> `127.0.0.1:8000/decs/`

* Redoc Documentation -> `127.0.0.1:8000/redoc/`


# SPDX-License-Identifier: (Apache-2.0 OR MIT)