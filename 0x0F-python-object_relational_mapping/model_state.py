#!/usr/bin/python3
"""The class definition State"""

from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State class"""
    __tablename__ = 'states'
    id = Column(Integer, Sequence('state_id_seq'), primary_key=True)
    name = Column(String(128), nullable=False)
