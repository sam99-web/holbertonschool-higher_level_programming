#!/usr/bin/python3
"""
9-model_state_filter_a.py
Script that lists all State objects,
That contain the letter a from the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    """
    Main function,
    """
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True
    )
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = (
        session.query(State).
        filter(State.name.like('%a%')).
        order_by(State.id).all()
    )

    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()

