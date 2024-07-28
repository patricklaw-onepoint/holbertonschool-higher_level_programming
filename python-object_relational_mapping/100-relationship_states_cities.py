#!/usr/bin/python3
"""creates the State “California” with the City “San Francisco”"""
from sys import argv
from relationship_city import City
from relationship_state import Base, State
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

    newState = State(name="California")
    session.add(newState)
    session.commit()

    newCity = City(name="San Francisco", state_id=newState.id)
    session.add(newCity)
    session.commit()
    session.close()
