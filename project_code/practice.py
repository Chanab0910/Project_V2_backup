from random import randint, shuffle, sample, random

from numpy import random
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from project_code.models import Country, Match,CountryMatch, Stage
from project_code.create_group_matches import GroupGenerator
engine = create_engine('sqlite:///World_cup.sqlite3', echo=True)
sess = Session(engine)

conn = engine.connect()

l = [1,5,3,4]

i = l.index(max(l))

print(i)
print(l[:i]+l[i+1:])

