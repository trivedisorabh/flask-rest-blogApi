
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Text, DateTime
from sqlalchemy.orm import relationship
import datetime


Base = declarative_base()

# The user model is kept basic.
# maybe add a realation to blogpost?
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True, nullable=False)
    email = Column(String(80), unique=True, nullable=False)
    password = Column(String(80))
    admin = Column(Boolean)
    test = Column(String(50))

# The blogpost model is simple, but contains ForeignKey for relations to users
# Should also contain a relation to comment feature...

class Blogpost(Base):
    __tablename__ = "blogpost"
    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    content = Column(Text, nullable=False)
    author_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    modified_at = Column(DateTime, default=datetime.datetime.utcnow())
    category = relationship('Category', backref='blogpost')
    comment = relationship('Comment', backref='blogpost')


class Category(Base):
    __tablename__ = "category"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    blogpost_id = Column(Integer, ForeignKey('blogpost.id'))


# just temporary... need to make this spam safe.
class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True)
    email = Column(String(50), nullable=False)
    content = Column(String(200), nullable=False)
    blogpost_id = Column(Integer, ForeignKey('blogpost.id'))
    created_at = Column(DateTime, default=datetime.datetime.utcnow())


# table for handling blacklisted tokens.
class BlacklistToken(Base):
    __tablename__ = "blacklist_tokens"
    id = Column(Integer, primary_key=True)
    token = Column(String(500), unique=True, nullable=False)
    blacklisted_on = Column(DateTime, default=datetime.datetime.now())
