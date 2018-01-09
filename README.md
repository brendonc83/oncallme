# oncallme

An app to log your on call hours.

Database - PostGreSQL
Web Framework - Django
Frontend - Bootstrap

WIP


Setup
-----

```
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

In order to install mock you may need to update your versions of pip, wheel and setuptools. After creating your virtual environment the following command will do the trick:

```
$ pip install -U pip wheel setuptools
```

```
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
python manage.py runserver
```
