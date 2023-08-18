#!/usr/bin/python3
'''
    defining City class for mapping in database
'''
from sqlalchemy import Column, String, Integer, ForeignKey
from relationship_state import State, Base
from sqlalchemy.orm import DeclarativeBase, relationship


class City(Base):
    '''
    state class

    atts:
         tablename (str): name in database
         id (int): instance id
         name (str): instance name
         state_id (int): represent states id from states table
    '''
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
