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

    Session = sessionmaker(bind=engine)
    flag = 1
    conn = Session()
    for state in conn.query(State).order_by(State.id).all():
        if sys.argv[4] == state.name:
            flag = 0
            print("{}".format(state.id))
    if flag == 1:
        print("Not found")
    conn.close()
