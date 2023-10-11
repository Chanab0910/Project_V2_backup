from numpy import random
from random import randint, shuffle, sample

import numpy as numpy
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


class GroupGenerator:
    def __init__(self):
        self.engine = self.create_engine('sqlite:///World_cup.sqlite3', echo=True)

        self.sess = self.Session(self.engine)
        self.team = ''
        self.groups = [[] for i in range(8)]
        self.country = self.sess.query(self.Country).first()

        self.countries = [sample(self.sess.query(self.Country).filter_by(tier=i).all()) for i in range(4)]

    def group_draw(self):
        group = []
        for i, group in enumerate(self.groups):
            self.team = self.countries[i][randint(0, len(self.countries[i]))]
            group.append(self.team)
            self.countries[i].remove(self.team)
        return group


class SimulateGroups:
    def __init__(self):
        self.order = [[1,3], [2,4], [1,4],[2,3],[3,4],[1,2]]
        self.Home_team_score = None
        self.base = 0.0128125
        self.groups = self.GroupGenerator.group_draw()
        self.engine = self.create_engine('sqlite:///World_cup.sqlite3', echo=True)

        self.sess = self.Session(self.engine)

    def sim_match(self):

        for group in self.groups:
            for i, matches in enumerate(group):
                if self.calculate_goals(
                        self.sess.query(self.Country.Attack).filter_by(
                            self.Country.Country_name == matches[self.order[i][0]]),
                        self.sess.query(self.Country.Defense).filter_by(
                            self.Country.Country_name == matches[self.order[i][1]])) > self.calculate_goals(
                    self.sess.query(self.Country.Attack).filter_by(self.Country.Country_name == matches[self.order[i][1]]),
                    self.sess.query(self.Country.Defense).filter_by(self.Country.Country_name == matches[self.order[i][0]])):
                    ...
                    


    def calculate_goals(self, attack, defense):
        self.goals = random.poisson(self.base * (attack/defense))
        return self.goals

    def __repr__(self):
        return f'{self.goals}'
