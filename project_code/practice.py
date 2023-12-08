from random import randint, shuffle, sample, random

from numpy import random
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from project_code.models import Country, Match,CountryMatch, Stage
from project_code.create_group_matches import GroupGenerator
engine = create_engine('sqlite:///World_cup.sqlite3', echo=True)
sess = Session(engine)

conn = engine.connect()

match_id = 3
teams_id = [13, 12]

score = (4, 3)

country_matches = sess.query(CountryMatch).filter_by(match_id=4).all()

country_matches[0].score = score[0]
country_matches[1].score = score[1]

if score[0] > score[1]:
    country_matches[0].result = 'win'
    country_matches[1].result = 'loss'
elif score[1] > score[0]:
    country_matches[0].result = 'loss'
    country_matches[1].result = 'win'
else:
    country_matches[0].result = 'loss'
    country_matches[1].result = 'win'
