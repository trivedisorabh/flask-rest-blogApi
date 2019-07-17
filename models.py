from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, text
import datetime


Base = declarative_base()

# The user model is kept basic.
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True, nullable=False)
    email = Column(String(80), unique=True, nullable=False)
    password = Column(String(80))
    admin = Column(Boolean)

# The blogpost model is simple, but contains ForeignKey for relations to users
# Should also contain a relation to comment feature... 

class Blogpost(Base):
    __tablename__ = "blogpost"
    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    content = Column(text, nullable=False)
    author_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    created_at = Column(Datetime)
    modified_at = Column(datetime)
