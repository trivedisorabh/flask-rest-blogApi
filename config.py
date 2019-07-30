#configuration file for the flask app.
#add new configurations here
class Config(object):
    SQLALCHEMY_DATABASE_URI = 'postgresql://robert:moss@localhost/blog_api_db'
    SECRET_KEY = 'thisissecret'

# DATABASE_URI = 'postgresql://robert:moss@localhost/blog_api_db'
