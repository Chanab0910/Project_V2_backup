from random import randint, shuffle, sample, random

from numpy import random
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from run_group_matches import MakeMatches
from project_code.models import Country, Match, CountryMatch, Stage
from project_code.create_group_matches import GroupGenerator
from find_group_results import FindGroupResults


class Knockouts:
    def __init__(self):
        self.find_group_results = FindGroupResults()
        self.list_of_first_place = self.find_group_results.came_first
        self.list_of_second_place = self.find_group_results.came_second
        self.engine = create_engine('sqlite:///World_cup.sqlite3', echo=True)
        self.sess = Session(self.engine)

    def randomise_lists(self):
        self.list_of_first_place = sample(self.list_of_first_place, k=len(self.list_of_first_place))
        self.list_of_second_place = sample(self.list_of_second_place, k=len(self.list_of_second_place))

    def sim_round(self):
        for
            ...