from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from models_2 import Country, Group

engine = create_engine('sqlite:///World_cup_2.sqlite3', echo=True)

sess = Session(engine)

countries = sess.query(Country).all()
groups = sess.query(Group).all()

australia = groups[0]
austria = groups[0]
belgium = groups[0]
canada = groups[0]
print('\n')
print('\n')
print(groups[0].countries)
print('\n')


"""simulate a game 
result = sim_match(australia,belgium)"""

sess.commit()
sess.close()


