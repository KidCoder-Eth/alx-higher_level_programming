#!/usr/bin/python3
"""script that creates the State “California” with the City “San Francisco”
    from the database hbtn_0e_100_usa: (100-relationship_states_cities.py)
    """
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City, Base

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
    storing = State(name='California')
    storing.cities = [City(name='San Francisco')]
    session.add(storing)
    session.commit()
    session.close()
