# Simple flask restfull blog-Api

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## About
This blog-api is a learning project for using flask as backend and for making a RESTfull api with JWT authentication.<br>
It will also serve as a part of my personal webpage<br>
The project is not finished, so please let me know if you see somthing you like to contribute to. You can also post a issue and look at the todo-list, its most welcome. <br>
__Todos:__<br>
 - review structure of the project
 - Update readme
 - Look at best practice to do DB migrations
 - Add a logout route.

## How to run the API

__Built with:__

- [Flask](https://github.com/pallets/flask)
- [SQLAlchemy](https://github.com/pallets/flask-sqlalchemy)
- [JWT](https://github.com/jpadilla/pyjwt)
- [pipenv](https://pipenv.readthedocs.io/en/latest/)
- [sqlalchemy-media](https://pypi.org/project/sqlalchemy-media/)
- [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/)

__Install:__

Clone the repo and setup with pipenv<br>
```
$ brew install pipenv
$ cd toTheProject
$ pipenv --python 3.6
$ pipenv install requests
```

Change configuration variables in config.py according to your work environment<br>
You set your variables from the command line like this(for OSX):
```
$ export DATABASE_URI= 'read the docs on your choice of DB'
$ export SECRET_KEY = 'thisissecret'
```
The config file is handling the environment variables like this:
```python
class Config(object):
  SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
  SECRET_KEY = os.getenv('SECRET_KEY')
```

Now your project should be oki to run.<br>
Documentation on the endpoints are under construction.

Run the application with

```
$ flask run
```

__API Documentation:__
