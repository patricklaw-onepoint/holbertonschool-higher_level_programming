#!/usr/bin/python3
"""adds the State object “Louisiana” to the database"""
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

    newState = State(name="Louisiana")
    session.add(newState)
    session.commit()
    print(newState.id)
