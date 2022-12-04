#!/usr/bin/python3
"""script that deletes all State objects with a name containing
    the letter a from the database hbtn_0e_6_usa
    """

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

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
    states = session.query(State).filter(
        State.name.like('%a%')).delete(synchronize_session=False)
    session.commit()
    session.close()
