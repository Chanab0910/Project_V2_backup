from random import randint, shuffle, sample, random

from numpy import random
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from code.models import Country, Match, Group_match, Country_match, Group_points
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
        self.order = [[0, 2], [1, 3], [2, 1], [0, 3], [0, 1], [2, 3]]
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
        # Takes each group and simulates it using simulate game and iterating through each game in the group
        for group in self.list_of_groups:
            self.group_id += 1
            print('\n')
            print('\n')
            print('\n')
            print(group[0], group[1], group[2], group[3])
            print('\n')
            print('\n')
            print('\n')
            self.create_group_points(group[0], group[1], group[2], group[3])
            for i in range(len(self.order)):
                self.sim_game(str(group[self.order[i - 1][0]])[8:-1], str(group[self.order[i - 1][1]])[8:-1])

    def sim_game(self, home_country, away_country):
        self.home_country_attack = self.get_attack(home_country)
        self.away_country_attack = self.get_attack(away_country)
        self.home_country_defense = self.get_defense(home_country)
        self.away_country_defense = self.get_defense(home_country)
        self.Home_team_score = self.calculate_goals(self.home_country_attack[0], self.home_country_defense[0])
        self.Away_team_score = self.calculate_goals(self.away_country_attack[0], self.home_country_defense[0])
        if self.Home_team_score > self.Away_team_score:
            self.add_to_match(home_country)
            pass
        elif self.Home_team_score < self.Away_team_score:
            self.add_to_match(away_country)
            pass
        else:
            self.add_to_match('draw')
            pass
        self.add_to_country_match(home_country, away_country)
        self.add_to_group_match()
        # self.add_to_group()

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
        Get_match_id = self.sess.query(Match.Match_id).order_by(Match.Match_id.desc()).first()[0]

        self.country_match_input = Country_match(
            Match_id=Get_match_id,
            Home_team_id=self.sess.query(Country.country_id).filter_by(
                country_name=home_country),
            Away_team_id=self.sess.query(Country.country_id).filter_by(
                country_name=away_country))
        self.sess.add(self.country_match_input)
        self.sess.commit()

    def add_to_group_match(self):
        group_match_input = Group_match(Group_id=self.group_id, Match_id=
        self.sess.query(Match.Match_id).order_by(Match.Match_id.desc()).first()[0])
        self.sess.add(group_match_input)
        self.sess.commit()

    def add_to_group_points(self, winner):
        ...

    def create_group_points(self, team1, team2, team3, team4):
        create_new_group = Group_points(Group_id=self.group_id,
                                        team1_id=self.sess.query(Country.country_id).filter_by(country_name=str(team1)[8:-1]),
                                        team2_id=self.sess.query(Country.country_id).filter_by(country_name=str(team2)[8:-1]),
                                        team3_id=self.sess.query(Country.country_id).filter_by(country_name=str(team3)[8:-1]),
                                        team4_id=self.sess.query(Country.country_id).filter_by(country_name=str(team4)[8:-1]),
                                        team1_points=0,
                                        team2_points=0,
                                        team3_points=0,
                                        team4_points=0,
                                        )

        self.sess.add(create_new_group)
        self.sess.commit()

if __name__ == '__main__':
    gg = SimulateGroups()
    print(gg.groups_matches())
