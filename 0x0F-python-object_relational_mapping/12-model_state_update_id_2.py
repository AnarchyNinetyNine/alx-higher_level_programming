#!/usr/bin/python3

"""
    This script changes the name of the State where id = 2
    to 'New Mexico' in the database hbtn_0e_6_usa.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Create an engine to connect to the MySQL database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Bind the engine to the session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the State object with id = 2
    state = session.query(State).filter(State.id == 2).one_or_none()

    # Change the state's name to 'New Mexico' if it exists
    if state:
        state.name = "New Mexico"
        session.commit()
