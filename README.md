# Care2Donate

<https://care2donate.com/>

## Setup

* sudo apt-get install libpq-dev python-dev
* sudo apt-get install python-virtualenv
* sudo apt-get install postgresql postgresql-contrib

* virtualenv --python=python3 venv
* . venv/bin/activate
* pip install -r requirements.txt

* cp care2donate/config/config_tpl.py care2donate/config/config.py
* create database and user and change the values as required in care2donate/config/config.py
* ./manage.py migrate
* ./manage.py runserver

## Postgres

For MacOS:
    brew install --build-from-source postgresql@12
