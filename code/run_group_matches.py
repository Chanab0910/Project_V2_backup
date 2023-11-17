"""
This is used to loop through all the entries in country_match and put them through simulate_game
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import update
from sim_game import SimGame
from code.create_groups import GroupGenerator
from code.models import Country, CountryMatch, Match
import sqlite3


class MakeMatches:
    def __init__(self):
        self.group_generator = GroupGenerator()
        self.list_of_groups = []
        self.list_of_groups = self.group_generator.collate_groups()
        self.engine = create_engine('sqlite:///World_cup.sqlite3', echo=True)
        self.sess = Session(self.engine)
        self.country_match_objects = self.sess.query(CountryMatch).all()
        self.ids = []
        self.matches = []
        self.sim_game_class = SimGame()
        self.order = [[0], [2], [1], [3], [2], [1], [0], [3], [0], [1], [2], [3]]
        self.object_pair_list = []

    def creates_ids(self):
        # creates the ID for each entry and sends it to create_initial_country_match to commit
        for group in self.list_of_groups:
            for i in range(len(self.order) - 1):
                country_object = group[self.order[i][0]]
                country_object_id = country_object.country_id
                self.create_initial_country_match(country_object_id)

    def create_initial_country_match(self, id):
        # Commits the id
        add_to_country_match = CountryMatch(country_id=id)
        self.sess.add(add_to_country_match)
        self.sess.commit()

    def pairing(self, iterable):
        a = iter(iterable)
        return zip(a, a)
    """from stack overflow"""

    def pair_match_object(self, list_to_split):
        for a, b in self.pairing(list_to_split):
            self.matches.append([a, b])

    """from stack overflow"""

    def get_pair_list_of_objects(self):
        for group in self.list_of_groups:
            for i in range(len(self.order) - 1):
                country_object = group[self.order[i][0]]
                self.object_pair_list.append(country_object)
        return self.object_pair_list

    def sim_the_game(self):
        self.get_pair_list_of_objects()
        self.pair_match_object(self.object_pair_list)
        for i, match in enumerate(self.matches):
            print(self.sim_game_class.sim_game_object(match[0], match[1]))

if __name__ == '__main__':
    gg = MakeMatches()
    print(gg.sim_the_game())
