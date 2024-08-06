#!/usr/bin/python3

"""
This script deletes all State objects with a name containing the letter 'a'
from the database hbtn_0e_6_usa.
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

    # Query all State objects with a name containing the letter 'a'
    states = session.query(State).filter(State.name.like('%a%')).all()

    # Delete each State object found
    for state in states:
        session.delete(state)

    # Commit the session to apply changes to the database
    session.commit()
