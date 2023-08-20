#!/usr/bin/python3
'''
    Select query using sqlalchemy
'''
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import select, create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)()
    results = Session.query(State, City).join(City).order_by(State.id)
    for st, ct in results:
        print(f'{st.name}: ({ct.id}) {ct.name}')
