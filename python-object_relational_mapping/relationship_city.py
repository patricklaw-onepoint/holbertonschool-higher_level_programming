#!/usr/bin/python3
"""file that contains the class definition of
a City and an instance Base = declarative_base()"""
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base


class City(Base):
    """relationship cities table"""

    __tablename__ = "cities"
    id = Column(
        Integer,
        primary_key=True,
        nullable=False,
        autoincrement=True,
        unique=True,
    )
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
