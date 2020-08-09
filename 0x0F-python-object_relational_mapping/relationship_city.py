#!/usr/bin/python3
"""The class definition cities"""

from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from relationship_state import Base, State


class City(Base):
    """State cities"""
    __tablename__ = 'cities'
    id = Column(Integer, Sequence('city_id_seq'), primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
