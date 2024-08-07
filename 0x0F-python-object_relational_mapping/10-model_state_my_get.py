#!/usr/bin/python3

"""
    This script prints the State object with the name passed as an argument
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

    # Query the State object with the name passed as an argument
    state_name = sys.argv[4]
    state = (
                session.query(State)
                .filter(State.name == state_name)
                .one_or_none()
            )

    # Print the State object's id or 'Not found' if no state is found
    print(state.id if state else "Not found")
