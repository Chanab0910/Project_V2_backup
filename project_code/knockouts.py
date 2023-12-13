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
        self.list_of_first_place = self.find_group_results.came_first
        self.list_of_second_place = self.find_group_results.came_second
        self.engine = create_engine('sqlite:///World_cup.sqlite3', echo=True)
        self.sess = Session(self.engine)
        self.create_matches = CreateMatches()
        self.match_id = self.create_matches.match_id
        self.sim_game_class = SimGame()


    def randomise_lists(self):
        self.list_of_first_place = sample(self.list_of_first_place, k=len(self.list_of_first_place))
        self.list_of_second_place = sample(self.list_of_second_place, k=len(self.list_of_second_place))

    def sim_round(self):
        for i in range(len(self.list_of_first_place)):

            add_to_country_match1 = CountryMatch(match_id = self.match_id, country_id = self.list_of_first_place[0])
            add_to_country_match2 = CountryMatch(match_id=self.match_id, country_id=self.list_of_second_place[0])

            self.sess.add(add_to_country_match1)
            self.sess.add(add_to_country_match2)
            self.sess.commit()
            result = self.sim_game_class.sim_game_object(self.list_of_first_place[0],self.list_of_second_place[0], stage=9+i, match_number=1)
            print(result)
            self.list_of_first_place[0].pop()
            self.list_of_second_place[0].pop()


    def collate(self):
        self.randomise_lists()
        print(self.sim_round())

if __name__ == '__main__':
    gg = Knockouts()
    print(gg.collate())



