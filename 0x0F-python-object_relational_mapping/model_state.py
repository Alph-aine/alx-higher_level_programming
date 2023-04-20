#!/usr/bin/python3
''' creates a database table using ORM(slqalchemy) '''
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base


'''defines the base class to inherit from later'''
Base = declarative_base()

class State(Base):
    '''This class defines the table and its fields'''
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, unique=True,
                autoincrement=True)
    name = Column(String(128), nullable=False)
