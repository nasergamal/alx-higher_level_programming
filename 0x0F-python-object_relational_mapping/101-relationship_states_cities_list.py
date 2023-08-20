#!/usr/bin/python3
"""
    Start link class to table in database
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)()
    result = Session.query(State).order_by(State.id)
    for s in result:
        print(f'{s.id}: {s.name}')
        for row in s.cities:
            print(f'\t{row.id}: {row.name}')
