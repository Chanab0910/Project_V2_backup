from random import randint, sample

from numpy import random
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from project_code.models import Country, Match, CountryMatch


class GroupGenerator:
    def __init__(self):
        self.engine = create_engine('sqlite:///World_cup.sqlite3', echo=True)

        self.sess = Session(self.engine)
        self.team = ''
        self.country = self.sess.query(Country).first()

        self.countries = [sample(self.sess.query(Country).filter_by(tier=i + 1).all(),
                                 k=len(self.sess.query(Country).filter_by(tier=i + 1).all())) for i in range(4)]

    def group_draw(self):
        # Creates a single group by taking a random country from each tier and adding it to a list
        group = []
        for i, tier in enumerate(self.countries):
            self.team = tier[randint(0, len(tier) - 1)]
            group.append(self.team)
            tier.remove(self.team)
        return group

    def collate_groups(self):
        # Iterates through group_draw and creates all 8 groups and then adds it to collated groups to make one big
        # list of lists.
        collated_groups = []
        for i in range(8):
            collated_groups.append(self.group_draw())

        return collated_groups


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
            for i in range(len(self.order)):
                country_object = group[self.order[i][0]]
                country_object_id = country_object.country_id
                self.create_initial_country_match(country_object_id)

    def create_initial_country_match(self, id):
        # Commits the id
        add_to_country_match = CountryMatch(country_id=id)
        self.sess.add(add_to_country_match)
        self.sess.commit()


if __name__ == '__main__':
    ff = GroupGenerator()
    print(ff.collate_groups())
    gg = CreateMatches()
    print(gg.creates_ids())
