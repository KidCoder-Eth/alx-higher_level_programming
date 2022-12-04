#!/usr/bin/python3
"""script that lists all State objects from the database hbtn_0e_6_usa
    """
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    """Main function
    """
    MY_USER = argv[1]
    MY_PWD = argv[2]
    MY_DB = argv[3]
    MY_HOST = 'localhost'
    engine = create_engine(
        f"mysql+mysqldb://{MY_USER}:{MY_PWD}@{MY_HOST}/{MY_DB}",
        pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State).order_by(State.id)
    [print(f'{state.id}: {state.name}') for state in result]
