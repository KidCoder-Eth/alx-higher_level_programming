#!/usr/bin/python3
"""script 14-model_city_fetch_by_state.py that prints all City objects
from the database hbtn_0e_14_usa:
    """

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import Base, City
from model_state import State

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
    result = session.query(City, State).filter(
        City.state_id == State.id).order_by(City.id)
    [print(f'{state.name}: ({city.id}) {city.name}') for city, state in result]
    session.close()
