from random import randint, shuffle, sample

import numpy.random
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


from code.models import Country, Match, Group, Country_match


class SimulateGroups():
    def __init__(self):
        self.Away_team_score = None
        self.goals = None
        self.collated_groups = []
        self.away_country_defense = None
        self.away_country_attack = None
        self.home_country_defense = None
        self.home_country_attack = None
        self.defense = None
        self.attack = None
        self.Home_team_score = None
        self.base = 0.0128125
        self.engine = create_engine('sqlite:///World_cup.sqlite3', echo=True)
        self.order = [[1, 3], [2, 4], [3, 2], [1, 4], [1, 2], [3, 4]]
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
        for i in range(8):
            self.collated_groups.append(self.group_draw())
        self.collated_groups = self.collated_groups[0]
        self.collated_groups = [self.collated_groups[x:x + 4] for x in range(0, len(self.collated_groups), 4)]
        return self.collated_groups

    def get_attack(self, country):
        self.attack = self.sess.query(Country.attack).filter_by(Country.country_name == country)
        return self.attack

    def get_defense(self, country):
        self.defense = self.sess.query(Country.defense).filter_by(Country.country_name == country)
        return self.defense

    def groups_matches(self):
        for group in self.collated_groups:
            for i in range(len(self.order)):
                self.sim_game(group[self.order[i][0]], group[self.order[i][1]])

    def sim_game(self, home_country, away_country):
        self.home_country_attack = self.get_attack(home_country)
        self.away_country_attack = self.get_attack(away_country)
        self.home_country_defense = self.get_defense(home_country)
        self.away_country_defense = self.get_defense(home_country)
        self.Home_team_score = self.calculate_goals(self.home_country_attack, self.home_country_defense)
        self.Away_team_score =self.calculate_goals(self.away_country_attack, self.home_country_defense)

        if self.Home_team_score>self.Away_team_score:
            self.match_input = Match(Stage=1,Home_goals=self.Home_team_score,Away_goals=self.Away_team_score, Winner=home_country)
        elif self.Home_team_score<self.Away_team_score:
            self.match_input = Match(Stage=1,Home_goals=self.Home_team_score,Away_goals=self.Away_team_score, Winner=away_country)
        else:
            self.match_input = Match(Stage=1, Home_goals=self.Home_team_score, Away_goals=self.Away_team_score,
                                     Winner='draw')

    def calculate_goals(self, attack, defense):
        self.goals = numpy.random.poisson((self.base * (attack / defense)) * 90)
        return self.goals


if __name__ == '__main__':
    gg = SimulateGroups()
    print(gg.collate_groups())
