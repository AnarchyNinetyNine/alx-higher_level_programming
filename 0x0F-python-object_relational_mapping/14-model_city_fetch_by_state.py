#!/usr/bin/python3

"""
    This script prints all City objects from the database hbtn_0e_14_usa,
    sorted in ascending order by cities.id.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    # Create an engine to connect to the MySQL database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Bind the engine to the session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all City objects, join with State, and sort by cities.id
    results = (
                session.query(City, State).
                join(State, City.state_id == State.id)
                .order_by(City.id)
                .all()
            )

    # Print each City object in the required format
    for city, state in results:
        print(f"{state.name}: ({city.id}) {city.name}")
