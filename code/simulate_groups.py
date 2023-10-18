from random import randint, shuffle, sample

import numpy.random
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from code.create_groups import GroupGenerator
from code.models import Country

class SimulateGroups(GroupGenerator):
    def __init__(self, group_generator):
        self.away_country_defense = None
        self.away_country_attack = None
        self.home_country_defense = None
        self.home_country_attack = None
        self.defense = None
        self.attack = None
        self.Home_team_score = None
        self.base = 0.0128125
        self.groups = group_generator.collated_group
        self.engine = create_engine('sqlite:///World_cup_1.sqlite3', echo=True)
        self.order = [[1, 3], [2, 4], [3, 2], [1, 4], [1, 2], [3, 4]]
        self.sess = Session(self.engine)

    def get_attack(self, country):
        self.attack = self.sess.query(Country.Attack).filter_by(Country.Country_name == country)
        return self.attack

    def get_defense(self, country):
        self.defense = self.sess.query(Country.Defense).filter_by(Country.Country_name == country)
        return self.defense

    def game_order(self):
        for group in self.groups:
            for i in range(len(self.order)):
                self.sim_game(group[self.order[i][0]], group[self.order[i][1]])

    def sim_game(self, home_country, away_country):
        self.home_country_attack = self.get_attack(home_country)
        self.away_country_attack = self.get_attack(away_country)
        self.home_country_defense = self.get_defense(home_country)
        self.away_country_defense = self.get_defense(home_country)

        if self.calculate_goals(self.home_country_attack,self.home_country_defense) > self.calculate_goals(self.away_country_attack, self.home_country_defense):
            ...

    def calculate_goals(self, attack, defense):
        self.goals = numpy.random.poisson((self.base * (attack / defense)) * 90)
        return self.goals


if __name__ == '__main__':
    gg = SimulateGroups(group_generator)
    print(gg.get_attack('England'))