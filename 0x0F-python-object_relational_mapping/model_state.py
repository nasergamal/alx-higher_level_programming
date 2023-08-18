#!/usr/bin/python
'''
    defining states class for mapping in database
'''
from sqlalchemy import Column, Integer, String
# from sqlalchemy.ext.declarative import declarative_base
# Base = declarative_base()
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    '''ORM Base'''
    pass


class State(Base):
    '''state class

       atts:
            tablename (str): name in database
            id (int): instance id
            name (str): instance name

    '''
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
