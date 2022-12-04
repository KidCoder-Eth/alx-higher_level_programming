#!/usr/bin/python3
"""Defines city model
    """
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.sql.schema import ForeignKey

Base = declarative_base()


class City(Base):
    """This is the schema of city entity in the db"""
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
