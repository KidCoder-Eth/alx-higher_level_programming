#!/usr/bin/python3
"""script that lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa
    """
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import Base, City
from relationship_state import State

if __name__ == '__main__':
    """Main function
    """
    MY_HOST = 'localhost'
    MY_USER = argv[1]
    MY_PASS = argv[2]
    MY_DB = argv[3]
    engine = create_engine(
        f'mysql+mysqldb://{MY_USER}:{MY_PASS}@{MY_HOST}/{MY_DB}',
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State)
    for state in states:
        print(f'{state.id}: {state.name}')
        for city in state.cities:
            print(' '*4+f'{city.id}: {city.name}')
    session.close()
