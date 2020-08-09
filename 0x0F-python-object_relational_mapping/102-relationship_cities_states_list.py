#!/usr/bin/python3
"""From city"""
import sys
from relationship_state import Base, State
from relationship_city import City

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    r = session.query(State, City).join(City, State.id ==
                                        City.state_id).order_by(City.id).all()
    for result in r:
        print("{}: {} -> {}".format(result[1].id, result[1].name,
                                    result[0].name))
    session.close()
