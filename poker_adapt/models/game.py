#!/usr/bin/python3
""" holds class Game"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
# from hashlib import md5


class Game(BaseModel, Base):
    """Representation of a game """
    if models.storage_t == 'db':
        __tablename__ = 'pokers'
        status = Column(String(20), nullable=True)
        hand_name = Column(String(30), nullable=True)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    else:
        status = ""
        hand_name = ""