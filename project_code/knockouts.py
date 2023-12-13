from random import randint, shuffle, sample, random

from numpy import random
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from run_group_matches import MakeMatches
from project_code.models import Country, Match, CountryMatch, Stage

from find_group_results import FindGroupResults
from create_group_matches import CreateMatches
from sim_game import SimGame


class Knockouts:
    def __init__(self):
        self.find_group_results = FindGroupResults()
        self.first_and_second_list = self.find_group_results.collective()
        self.list_of_first_place = self.first_and_second_list[0]
        self.list_of_second_place = self.first_and_second_list[1]
        self.engine = create_engine('sqlite:///World_cup.sqlite3', echo=True)
        self.sess = Session(self.engine)
        self.create_matches = CreateMatches()
        self.match_id = self.sess.query(CountryMatch.match_id).order_by(CountryMatch.match_id.desc()).first()
        self.sim_game_class = SimGame()
        self.match_id = self.match_id[0] + 1

    def randomise_lists(self):
        self.list_of_first_place = sample(self.list_of_first_place, k=len(self.list_of_first_place))
        self.list_of_second_place = sample(self.list_of_second_place, k=len(self.list_of_second_place))

    def sim_round(self):
        for i in range(len(self.list_of_first_place)):

            result = self.sim_game_class.sim_game_object(self.list_of_first_place[0], self.list_of_second_place[0],
                                                         stage=9 + i, match_number=1)
            first_goals = result[1]
            second_goals = result[2]

            result = self.get_winner(first_goals, second_goals)

            self.add_to_country_match(self.list_of_first_place[0].country_id, first_goals, result[0])
            self.add_to_country_match(self.list_of_second_place[0].country_id, second_goals, result[1])

            self.list_of_first_place.pop(0)
            self.list_of_second_place.pop(0)
            self.match_id+=1

    def get_winner(self, first_goals, second_goals):
        if first_goals > second_goals:
            first_result = 'win'
            second_result = 'loss'
        elif first_goals < second_goals:
            first_result = 'loss'
            second_result = 'win'
        else:
            first_result = 'draw'
            second_result = 'draw'
        return first_result, second_result

    def add_to_country_match(self, country_id, score, result):
        add_to_country_match = CountryMatch(country_id=country_id, match_id=self.match_id, score = score, result = result)
        self.sess.add(add_to_country_match)
        self.sess.commit()

    def collate(self):
        self.randomise_lists()
        self.sim_round()


if __name__ == '__main__':
    gg = Knockouts()
    print(gg.collate())
