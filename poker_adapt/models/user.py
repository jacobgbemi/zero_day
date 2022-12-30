#!/usr/bin/python3
""" holds class User"""
import models
from models.base_model import BaseModel, Base
# from os import getenv
# import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
# from hashlib import md5


class User(BaseModel, Base):
    """Representation of a user """
    if models.storage_t == 'db':
        __tablename__ = 'users'
        username = Column(String(20), unique=True, nullable=False)
        email = Column(String(120), unique=True, nullable=False)
        # image_file = Column(String(20), nullable=False, default='default.jpg')
        # password = Column(String(60), nullable=False)
        posts = relationship('Post', backref='user', lazy=True)
        pokers = relationship('Game', backref='user', lazy=True)
    else:
        username = ""
        email = ""
        image_file = ""
        password = ""

    