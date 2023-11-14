from random import randint, shuffle, sample

from numpy import random
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from code.models import Country, Match, CountryMatch
from create_groups import GroupGenerator


class CreateMatches:
    # Fills in intial information so that it lays out which matches play in what order and makes it easy to simulate
    # through all games
    def __init__(self):
        self.group_generator = GroupGenerator()
        self.list_of_groups = []
        self.list_of_groups = self.group_generator.collate_groups()
        self.engine = create_engine('sqlite:///World_cup.sqlite3', echo=True)
        self.sess = Session(self.engine)
        self.order = [[0], [2], [1], [3], [2], [1], [0], [3], [0], [1], [2], [3]]

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


if __name__ == '__main__':
    gg = CreateMatches()
    print(gg.creates_ids())
