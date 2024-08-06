#!/usr/bin/python3

"""
    This module connects to a MySQL database and lists all State objects.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    # Create an engine to connect to the MySQL database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Create all tables in the engine (if they don't exist already)
    Base.metadata.create_all(engine)

    # Bind the engine to the session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all State objects from the database
    states = session.query(State).all()

    # Print each State object
    for state in states:
        print(f"{state.id}: {state.name}")
