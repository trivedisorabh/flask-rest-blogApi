# Simple flask restfull blog-Api

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## About
This blog-api is a learning project for using flask as backend and for making a RESTfull api with JWT authentication.<br>
It will also serve as a part of my personal webpage<br>
The project is not finished, so please let me know if you see somthing you like to contribute to. You can also post a issue and look at the todo-list, its most welcome. <br>
__Todos:__<br>
 - write code for the missing models. Blogpost, comments.
 - setup environment variables
 - review structure of the project
 - Look at pest practice to do DB migrations
 - Add a logout route.

## How to run the API

__Built with:__

- [Flask](https://github.com/pallets/flask)
- [SQLAlchemy](https://github.com/pallets/flask-sqlalchemy)
- [JWT](https://github.com/jpadilla/pyjwt)
- [pipenv](https://pipenv.readthedocs.io/en/latest/)
-[sqlalchemy-media](https://pypi.org/project/sqlalchemy-media/)

__Install:__

Clone the repo and setup with pipenv<br>
```
$ brew install pipenv
$ cd toTheProject
$ pipenv --python 3.6
$ pipenv install requests
```

Change configuration variables in config.py according to your work environment<br>
```
SQLALCHEMY_DATABASE_URI = 'postgresql://robert:moss@localhost/blog_api_db'
SECRET_KEY = 'thisissecret'
DATABASE_URI = 'postgresql://robert:moss@localhost/blog_api_db'

```


Now your project should be oki to run.<br>
Documentation on the endpoints are under construction.

Run the application with

```
$ flask run
```
