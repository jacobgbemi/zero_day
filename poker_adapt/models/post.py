#!/usr/bin/python3
""" holds class Post"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Text, Integer, ForeignKey
from sqlalchemy.orm import relationship
from hashlib import md5


class Post(BaseModel, Base):
    """Representation of a post """
    if models.storage_t == 'db':
        __tablename__ = 'posts'
        title = Column(String(100), nullable=False)
        content = Column(Text, nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    else:
        title = ""
        content = ""