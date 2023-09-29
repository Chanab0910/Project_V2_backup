import pytest
from create_groups import GroupGenerator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Country, Match
import models as m
import random

# Connect to the activities database
engine = create_engine('sqlite:///:memory:', echo=True)

Session = sessionmaker(bind=engine)


countries = [m.Country(country_name='England', attack=78, defense=85, tier=1),
             # Country('Spain', 87, 83, 2),
             # Country('Germany', 81, 79, 3),
             # Country('Sweden', 78, 76, 4)
             ]