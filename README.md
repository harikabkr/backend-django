# Chat Backend Service

- Build using Django Framework


## Steps to create and start a Django Project

* Create a virtual env for python project

`pip install virtualenv` -- download virtual env library

`virtualenv chatenv` -- Will create a new python virtual env for the project

* Activate virtualenv everytime before you start the project

`chatenv\scripts\activate` -- RUN this everytime before starting the project this will make sure you are running in virtual env

`pip install django` -- To install django required only once.

` django-admin startproject chatBackendService` -- to start a new django project

`python manage.py makemigrations` -- Need to run this command when you change anything related to database, this creates migrations

`python manage.py migrate` -- Need to run this command when you change anything related to database, this applies migrations to the app

`python manage.py runserver` -- use this command to run the django app.

`django-admin startapp chatapi` -- create a new application for the api service.

`pip install djangorestframework django-cors-headers` -- install required libraries for API.

`pip install python-dotenv requests mysqlclient` -- 

`pip freeze > requirements.txt` command to get all he dependencies to one requirements.txt file.


## References
- Create an API using Django Rest framework, https://blog.logrocket.com/django-rest-framework-create-api/
- Integrate React and Django, https://www.digitalocean.com/community/tutorials/build-a-to-do-application-using-django-and-react
- Integrate Chat GPT with Django, https://testdriven.io/blog/python-openai-chatgpt/
- MySql with Django, https://www.askpython.com/django/django-mysql
- Django Rest framework Models, https://corgibytes.com/blog/2022/06/14/model-relationships-django-rest-framework/

