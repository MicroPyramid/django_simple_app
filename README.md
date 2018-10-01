Django Simple Application
=========================

Easy steps to install Django and create a new project.

Installation - Requirements
===========================

Install dependencies
---------------------------------

```
    $ sudo apt-get install python-setuptools python-dev build-essential
```

```
    $ sudo apt-get install python-pip python-virtualenv
```

To create virtual environment use the following  command

```
    $ virtualenv <env-name>
```

Active the virtualenvironment use the following command
```
    $ source <env-name>/bin/activate
```

Install Django
```
    $ pip install django
```

Create project in Django
```
    $ django-admin startproject simple_app
```

Run the project
```
    $ python manage.py runserver
```
