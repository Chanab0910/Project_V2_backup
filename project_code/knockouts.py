from random import randint, shuffle, sample, random

from numpy import random
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from run_group_matches import MakeMatches
from project_code.models import Country, Match, CountryMatch, Stage

from redo_find_group_results import FindGroupResults
from create_group_matches import CreateMatches
from sim_game import SimGame


class Knockouts:
    def __init__(self):
        self.match_id = None
        self.winner = []
        self.find_group_results = FindGroupResults()
        self.first_and_second_list = self.find_group_results.collective()
        self.list_of_first_place = self.first_and_second_list[0]
        self.list_of_second_place = self.first_and_second_list[1]
        self.engine = create_engine('sqlite:///World_cup.sqlite3', echo=True)
        self.sess = Session(self.engine)
        self.create_matches = CreateMatches()
        self.sim_game_class = SimGame()
        
        self.qf_list = []
        self.sf_list = []
        self.final_list = []

    def randomise_lists(self):
        self.list_of_first_place = sample(self.list_of_first_place, k=len(self.list_of_first_place))
        self.list_of_second_place = sample(self.list_of_second_place, k=len(self.list_of_second_place))

    def first_round(self,sim_num):
        self.match_id = self.sess.query(CountryMatch.match_id).filter_by(simulation_number=sim_num).order_by(
            CountryMatch.match_id.desc()).first()
        self.match_id = self.match_id[0] + 1
        for i in range(len(self.list_of_first_place)):

            results = self.sim_game_class.sim_game_object(self.list_of_first_place[0], self.list_of_second_place[0],
                                                          stage=9 + i, match_number=1,sim_num=sim_num,match_id=self.match_id)
            first_goals = results[1]
            second_goals = results[2]

            result = self.get_winner(first_goals, second_goals)

            self.add_to_country_match(self.list_of_first_place[0].country_id, first_goals, result[0],sim_num)
            self.add_to_country_match(self.list_of_second_place[0].country_id, second_goals, result[1],sim_num)

            if result[0] == 'win':
                self.qf_list.append(self.list_of_first_place[0])
            else:
                self.qf_list.append(self.list_of_second_place[0])

            self.list_of_first_place.pop(0)
            self.list_of_second_place.pop(0)
            self.match_id += 1

    def other_rounds(self, round_list, iterations, stage_start, next_round_list,sim_num):
        for i in range(iterations):
            home_team = round_list[0]
            away_team = round_list[1]
            results = self.sim_game_class.sim_game_object(home_team, away_team,
                                                          stage=stage_start + i, match_number=1,sim_num=sim_num,match_id=self.match_id)
            home_goals = results[1]
            away_goals = results[2]

            result = self.get_winner(home_goals, away_goals)

            self.add_to_country_match(home_team.country_id, home_goals, result[0],sim_num)
            self.add_to_country_match(away_team.country_id, away_goals, result[1],sim_num)

            if result[0] == 'win':
                next_round_list.append(home_team)
            else:
                next_round_list.append(away_team)
            round_list.pop(0)
            round_list.pop(0)
            self.match_id+=1

    def get_winner(self, first_goals, second_goals):
        if first_goals > second_goals:
            first_result = 'win'
            second_result = 'loss'
        elif first_goals < second_goals:
            first_result = 'loss'
            second_result = 'win'
        return first_result, second_result

    def add_to_country_match(self, country_id, score, result,sim_num):
        add_to_country_match = CountryMatch(country_id=country_id, match_id=self.match_id, score=score, result=result,simulation_number=sim_num)
        self.sess.add(add_to_country_match)
        self.sess.commit()

    def collate(self,sim_num):
        self.randomise_lists()
        self.first_round(sim_num)
        self.other_rounds(self.qf_list, 4, 17, self.sf_list,sim_num)
        self.other_rounds(self.sf_list,2, 21, self.final_list,sim_num)
        self.other_rounds(self.final_list,1,23,self.winner,sim_num)
        print(self.winner)

if __name__ == '__main__':
    gg = Knockouts()
    print(gg.collate(1))
