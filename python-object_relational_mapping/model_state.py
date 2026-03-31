#!/usr/bin/python3
"""
Contains the class definition of a State
and an instance Base = declarative_base()
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

# Instance de base pour toutes les classes SQLAlchemy
Base = declarative_base()


class State(Base):
    """
    State class:
    - links to the MySQL table 'states'
    - has 'id' (primary key, auto-increment, not null)
    - has 'name' (string, max 128 characters, not null)
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

