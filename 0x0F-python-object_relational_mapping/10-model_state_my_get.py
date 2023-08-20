#!/usr/bin/python3
'''
    Select query using sqlalchemy
'''
from sys import argv as a
from model_state import Base, State
from sqlalchemy import select, create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(a[1], a[2], a[3]))
    Session = (sessionmaker(bind=engine))()
    result = Session.query(State).filter(State.name == a[4]).first()
    if result:
        print(f'{result.id}')
    else:
        print('Not found')
