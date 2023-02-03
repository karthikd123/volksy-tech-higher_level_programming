#!/usr/bin/python3
"""Deletes into State obj from hbtn_0e_6_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


def delete_a_state_obj():
    engine = create_engine("mysql+mysqlhbtn_0e_6_usa://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)

    rows = session.query(State).all()

    for i in rows:
        if 'a' in i.__dict__['name']:
            session.delete(i)

    session.commit()

    session.close()


if __name__ == "__main__":
    delete_a_state_obj()i
