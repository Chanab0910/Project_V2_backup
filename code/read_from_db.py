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


countries = [sess.query(Country).filter_by(tier=i).all() for i in range(4)]




#tier1_countries = sess.query(Country).filter_by(tier=1).all()
#tier2_countries = sess.query(Country).filter_by(tier=2).all()
#tier3_countries = sess.query(Country).filter_by(tier=3).all()
#tier4_countries = sess.query(Country).filter_by(tier=4).all()

#countries_in_tiers = []
#countries_in_tiers.append(random.sample(tier1_countries, len(tier1_countries)))
#countries_in_tiers.append(random.sample(tier2_countries, len(tier2_countries)))
#countries_in_tiers.append(random.sample(tier3_countries, len(tier3_countries)))
#countries_in_tiers.append(random.sample(tier4_countries, len(tier4_countries)))

# x = sess.query(Country).filter_by(Country_name == tier4_countries[0]).all()
