#!/usr/bin/python3
"""deletes all State objects with a name containing the letter a"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost/{db_name}",
        pool_pre_ping=True,
    )

    # Create a session
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State):
        if "a" in state.name:
            session.delete(state)
    session.commit()
