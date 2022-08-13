#!/usr/bin/python3
"""
script that prints the State object
with the name passed as argument
 from the database hbtn_0e_6_usa
"""

if __name__ == "__main__":

    from sys import argv
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session

    if len(sys.argv) == 5:
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format
                               (sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)

    session = Session(engine)
    states = session.query(State).filter(State.name == argv[4]).first()

    if states is not None:
        print(states.id)

    else:
        print("Not found")
