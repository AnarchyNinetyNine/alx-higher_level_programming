#!/usr/bin/python3

"""
    This module defines the City class, which inherits from Base
    and links to the MySQL table 'cities'.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base


class City(Base):

    """
        City class that links to the 'cities' table in MySQL.

        Attributes:
            id (int): Auto-generated, unique integer, primary key.
            name (str): String of 128 characters, can't be null.
            state_id (int): Integer, can't be null, foreign key to states.id.
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
