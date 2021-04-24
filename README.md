
# GrowthPlug
Coding challenge by GrowthPlug.

  - Framework used Django(Python)
  - Database - SQLite
  - Facebook Graph API

### DEMO

[https://still-atoll-93918.herokuapp.com/](https://still-atoll-93918.herokuapp.com/)

### Installation

Requires [python](https://www.python.org/) 3+ to run.

After making virtual environment...

```sh
$ pip install -r requirements.txt

```

Create .env like .env.example in the project folder with appropriate values

To create database run
```sh
$ python manage.py migrate
```
To create superuser run
``
$ python manage.py createsuperuser
``

Facebook API requires the app to be in development mode for testing purposes. Ensure that you have satisfied all the requirements.

For Facebook authentication a third-party library [django-allauth](https://github.com/pennersr/django-allauth) is used. It requires app id and secret key of your Facebook app.

 Login to Django admin to configure Social Application model for Facebook provider.

