#!/usr/bin/python3

"""
    This script prints the first State object from the database hbtn_0e_6_usa.
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

    # Query the first State object from the database
    state = session.query(State).order_by(State.id).first()

    # Print the first State object or 'Nothing' if the table is empty
    print(state and f"{state.id}: {state.name}" or "Nothing")
