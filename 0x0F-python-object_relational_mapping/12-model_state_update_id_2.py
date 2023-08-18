#!/usr/bin/python3
'''
    Select query using sqlalchemy
'''
from sys import argv as a
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(a[1], a[2], a[3]))
    Session = (sessionmaker(bind=engine))()
    lou = State(name='Louisiana')
    result = Session.query(State).filter(State.id == 2).\
        update({State.name: 'New Mexico'}, synchronize_session=False)
    Session.commit()
