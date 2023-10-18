from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from code.models import Country

engine = create_engine('sqlite:///World_cup_1.sqlite3', echo=True)
sess = Session(engine)


def add_country(id,name, attack, defense, tier):
    country = Country(id = id,ountry_name='attack', attack=attack, defense=defense, tier=tier)
    return sess.add(country)

