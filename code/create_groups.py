from random import randint, shuffle, sample

import numpy.random
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from code.models import Country


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


if __name__ == '__main__':
    gg = GroupGenerator()
    print(gg.collate_groups())