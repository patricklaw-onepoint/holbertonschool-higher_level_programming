#!/usr/bin/python3
"""file that contains the class definition of
a City and an instance Base = declarative_base()
If the State object is deleted, all linked City
objects must be automatically deleted.
Also, the reference from a City object to
his State should be named state"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()


class State(Base):
    """relationship states table"""

    __tablename__ = "states"
    id = Column(
        Integer,
        primary_key=True,
        nullable=False,
        autoincrement=True,
        unique=True,
    )
    name = Column(String(128), nullable=False)
    cities = relationship(
        "City",
        cascade="all, delete-orphan",
        backref=backref("state", cascade="all"),
        single_parent=True,
    )
