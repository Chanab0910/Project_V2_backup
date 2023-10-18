from random import randint, shuffle, sample

import numpy.random
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from code.models import Country


class GroupGenerator:
    def __init__(self):
        self.engine = create_engine('sqlite:///World_cup_1.sqlite3', echo=True)

        self.sess = Session(self.engine)
        self.team = ''
        self.group = []
        self.country = self.sess.query(Country).first()

        self.countries = [sample(self.sess.query(Country).filter_by(tier=i + 1).all(),
                                 k=len(self.sess.query(Country).filter_by(tier=i + 1).all())) for i in range(4)]

    def group_draw(self):
        for i, group in enumerate(self.countries):
            self.team = group[randint(0, len(group) - 1)]
            self.group.append(self.team)
            group.remove(self.team)
        return self.group

    def collate_groups(self):
        self.collated_groups = []
        for i in range(8):
            self.collated_groups.append(self.group_draw())
        self.collated_groups = self.collated_groups[0]
        self.collated_groups = [self.collated_groups[x:x + 4] for x in range(0, len(self.collated_groups), 4)]
        return self.collated_groups



