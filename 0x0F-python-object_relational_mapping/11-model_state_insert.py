#!/usr/bin/python3

"""
    This script adds the State object 'Louisiana'
    to the database hbtn_0e_6_usa.
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

    # Create a new State object for "Louisiana"
    new_state = State(name="Louisiana")

    # Add the new State object to the session
    session.add(new_state)
    session.commit()

    # Print the new state's id
    print(new_state.id)
