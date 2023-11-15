"""
This is used to loop through all the entries in country_match and put them through simulate_game
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import update
from code.models import Country, CountryMatch, Match
import sqlite3


class MakeMatches:
    def __init__(self):
        self.engine = create_engine('sqlite:///World_cup.sqlite3', echo=True)
        self.sess = Session(self.engine)
        self.country_match_objects = self.sess.query(CountryMatch).all()
        self.ids = []
        self.matches = []

    def make_all_pairs(self):
        self.get_ids_in_list()
        self.pair_match_ids()
        print(self.matches)

    def get_ids_in_list(self):
        for i in range(len(self.country_match_objects)):
            self.ids.append(self.country_match_objects[i].country_id)
        return self.ids

    def pairwise(self, iterable):
        a = iter(iterable)
        return zip(a, a)

    def pair_match_ids(self):
        for x, y in self.pairwise(self.ids):
            self.matches.append([x,y])


    def make_match(self):
        self.match_input = """up"""


if __name__ == '__main__':
    gg = MakeMatches()
    print(gg.make_all_pairs())


