#!/usr/bin/python3
"""lists all State objects contain the letter a from the database hbtn_0e_6_usa
"""

if __name__ == '__main__':

    import sys
    from sqlalchemy import create_engine
    from model_state import Base, State
    from sqlalchemy.orm import Session

    if len(sys.argv) == 4:
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format
                               (sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)

    session = Session(engine)
    states = session.query(State)\
                    .filter(State.name.like('%a%')).order_by(State.id)

    for state in states:
        print("{}: {}".format(state.id, state.name))
