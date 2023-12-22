from random import randint, shuffle, sample, random

from numpy import random
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from analyse_results import Analyse
from project_code.models import Country, Match,CountryMatch, Stage
from project_code.create_group_matches import GroupGenerator
engine = create_engine('sqlite:///World_cup.sqlite3', echo=True)
sess = Session(engine)
analyse = Analyse()

conn = engine.connect()



g = [5,7,2,3]

highest_index = g.index(max(g))
group_list_minus_mx = g[:highest_index] + g[highest_index + 1:]

print(g[:highest_index])
print(g[highest_index + 1:])
print(group_list_minus_mx)