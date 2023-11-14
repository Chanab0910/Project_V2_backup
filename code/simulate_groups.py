from random import randint, shuffle, sample, random

from numpy import random
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from code.models import Country, Match
from create_groups import GroupGenerator


class SimulateGroups:
    def __init__(self):
        self.group_input = None
        self.group_id = 0
        self.country_match_input = None
        self.Away_team_score = None
        self.goals = None

        self.base = 0.0128125
        self.engine = create_engine('sqlite:///World_cup.sqlite3', echo=True)
        self.order = [[0, 2], [1, 3], [2, 1], [0, 3], [0, 1], [2, 3]]
        self.sess = Session(self.engine)
        self.team = ''
        self.group = []
        self.list_of_groups = []
        self.group_generator = GroupGenerator()
        self.list_of_groups = self.group_generator.collate_groups()

    def groups_matches(self):
        # Takes each group and simulates it using simulate game and iterating through each game in the group
        for group in self.list_of_groups:
            self.group_id += 1

            for i in range(len(self.order)):
                self.sim_game_object(group[self.order[i - 1][0]], group[self.order[i - 1][1]])

    def sim_game_object(self, home_country, away_country):
        # takes the object of each country, gets its attack and defense and runs each team through calculate goals.
        # It then determines who won
        home_country_attack = home_country.attack
        away_country_attack = away_country.attack
        home_country_defense = home_country.defense
        away_country_defense = away_country.defense
        Home_team_score = self.calculate_goals(home_country_attack, away_country_defense)
        Away_team_score = self.calculate_goals(away_country_attack, home_country_defense)
        if Home_team_score > Away_team_score:
            print('win')
            pass
        elif Home_team_score < Away_team_score:
            print('loss')
            pass
        else:
            print('draw')
            pass

    def calculate_goals(self, attack, defense):
        self.goals = random.poisson(90 * (self.base * (attack / defense)))
        return self.goals

if __name__ == '__main__':
    gg = SimulateGroups()
    print(gg.groups_matches())
