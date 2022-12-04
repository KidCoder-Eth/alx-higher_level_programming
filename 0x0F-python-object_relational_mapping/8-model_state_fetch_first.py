#!/usr/bin/python3
"""script that prints the first State object from the database
    hbtn_0e_6_usa
    """

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from model_state import State, Base
if __name__ == '__main__':
    MY_HOST = 'localhost'
    MY_USER = argv[1]
    MY_PASS = argv[2]
    MY_DB = argv[3]

    engine = create_engine(
        f'mysql+mysqldb://{MY_USER}:{MY_PASS}@{MY_HOST}/{MY_DB}',
        pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).order_by(State.id).first()
    if state:
        print(f'{state.id}: {state.name}')
    else:
        print('Nothing')
    session.close()