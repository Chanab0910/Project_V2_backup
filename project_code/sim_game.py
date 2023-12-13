from numpy import random
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from project_code.models import Match


class SimGame:
    def __init__(self):
        self.group_input = None
        self.group_id = 0
        self.country_match_input = None
        self.Away_team_score = None
        self.goals = None
        self.time = 90

        self.base = 0.0128125
        self.engine = create_engine('sqlite:///World_cup.sqlite3', echo=True)
        self.order = [[0, 2], [1, 3], [2, 1], [0, 3], [0, 1], [2, 3]]
        self.sess = Session(self.engine)
        self.team = ''

    def sim_game_object(self, home_country, away_country, stage, match_number):
        # takes the object of each country, gets its attack and defense and runs each team through calculate goals.
        # It then determines who won
        home_country_attack = home_country.attack
        away_country_attack = away_country.attack
        home_country_defense = home_country.defense
        away_country_defense = away_country.defense
        Home_team_score = self.calculate_goals(home_country_attack, away_country_defense)
        Away_team_score = self.calculate_goals(away_country_attack, home_country_defense)
        if Home_team_score > Away_team_score:
            self.add_to_match(stage, match_number)
            return 'win', Home_team_score, Away_team_score

        elif Home_team_score < Away_team_score:
            self.add_to_match(stage, match_number)
            return 'loss', Home_team_score, Away_team_score

        else:
            self.add_to_match(stage, match_number)
            return 'draw', Home_team_score, Away_team_score

    def calculate_goals(self, attack, defense):
        self.goals = random.poisson(self.time * (self.base * (attack / defense)))
        return self.goals

    def add_to_match(self, stage, match_number):
        match_addition = Match(stage_id=stage, match_number=match_number)
        self.sess.add(match_addition)
        self.sess.commit()
