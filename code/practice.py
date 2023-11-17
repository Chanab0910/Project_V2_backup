from random import randint, shuffle, sample, random

from numpy import random
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from code.models import Country, Match,CountryMatch, Stage
from code.create_groups import GroupGenerator
engine = create_engine('sqlite:///World_cup.sqlite3', echo=True)
sess = Session(engine)

conn = engine.connect()
stmt = CountryMatch.update().\
    values(points=3).\
    where(CountryMatch.country_id == 1)
conn.execute(stmt)