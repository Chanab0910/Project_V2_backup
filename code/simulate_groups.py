from random import randint, shuffle, sample, random

from numpy import random
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from code.models import Country, Match, Group_match, Country_match
from create_groups import GroupGenerator


class SimulateGroups:
    def __init__(self):
        self.group_input = None
        self.group_id = 0
        self.country_match_input = None
        self.Away_team_score = None
        self.goals = None
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

        self.list_of_groups = []

        self.countries = [sample(self.sess.query(Country).filter_by(tier=i + 1).all(),
                                 k=len(self.sess.query(Country).filter_by(tier=i + 1).all())) for i in range(4)]
        self.group_generator = GroupGenerator()
        self.list_of_groups = self.group_generator.collate_groups()

    def groups_matches(self):
        for group in self.list_of_groups:
            self.group_id += 1
            for i in range(len(self.order)):
                self.sim_game(str(group[self.order[i][0]]), str(group[self.order[i][1]]))

    def sim_game(self, home_country, away_country):
        self.home_country_attack = self.get_attack(home_country)
        self.away_country_attack = self.get_attack(away_country)
        self.home_country_defense = self.get_defense(home_country)
        self.away_country_defense = self.get_defense(home_country)
        self.Home_team_score = self.calculate_goals(self.home_country_attack, self.home_country_defense)
        self.Away_team_score = self.calculate_goals(self.away_country_attack, self.home_country_defense)
        if self.Home_team_score > self.Away_team_score:
            self.add_to_match(home_country)
        elif self.Home_team_score < self.Away_team_score:
            self.add_to_match(away_country)
        else:
            self.add_to_match('draw')
        self.add_to_country_match(home_country, away_country)
        self.add_to_group()

    def get_attack(self, country):
        self.attack = self.sess.query(Country.attack).filter_by(country_name=country).first()
        return self.attack

    def get_defense(self, country):
        self.defense = self.sess.query(Country.defense).filter_by(country_name=country).first()
        return self.defense

    def calculate_goals(self, attack, defense):
        self.goals = random.poisson(90 * (self.base * (attack / defense)))
        return self.goals

    def add_to_match(self, winner):
        match_input = Match(Stage=1, Home_goals=self.Home_team_score, Away_goals=self.Away_team_score,
                                 Winner=winner)
        self.sess.add(match_input)
        self.sess.commit()

    def add_to_country_match(self, home_country, away_country):
        self.country_match_input = Country_match(
            Home_team_id=self.sess.query(Country.country_id).filter_by(country_name=home_country),
            Away_team_id=self.sess.query(Country.country_id).filter_by(country_name=away_country))
        self.sess.add(self.country_match_input)
        self.sess.commit()

    def add_to_group(self):
        self.group_input = Group_match(self.group_id, self.sess.query(Match.Match_id).last())
        self.sess.add(self.group_input)
        self.sess.commit()


if __name__ == '__main__':
    gg = SimulateGroups()
    print(gg.groups_matches())
