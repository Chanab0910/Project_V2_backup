from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from models_2 import Country, Group

engine = create_engine('sqlite:///World_cup_2.sqlite3', echo=True)

sess = Session(engine)

countries = sess.query(Country).all()
groups = sess.query(Group).all()

australia = countries[0]
group_1 = groups[0]

australia.group = group_1
print(group_1.countries)

sess.commit()
sess.close()


