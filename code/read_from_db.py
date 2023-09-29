from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Country, Match
import random

# Connect to the activities database
engine = create_engine('sqlite:///World_cup_1.sqlite3', echo=True)

sess = Session(engine)
tier1 = []
count = 0

country = sess.query(Country).first()
countries = sess.query(Country).all()
tier1_countries = sess.query(Country).filter_by(Tier=1).all()
tier2_countries = sess.query(Country).filter_by(Tier=2).all()
tier3_countries = sess.query(Country).filter_by(Tier=3).all()
tier4_countries = sess.query(Country).filter_by(Tier=4).all()

# x = sess.query(Country).filter_by(Country_name == tier4_countries[0]).all()
