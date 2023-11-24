"""
This is used to loop through all the entries in country_match and put them through simulate_game
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import update
from sim_game import SimGame
from project_code.create_group_matches import GroupGenerator
from project_code.models import Country, CountryMatch
import sqlite3


class MakeMatches:
    def __init__(self):
        self.match_number = 0
        self.goals = None

        self.group_generator = GroupGenerator()
        self.list_of_groups = []
        self.list_of_groups = self.group_generator.collate_groups()
        self.engine = create_engine('sqlite:///World_cup.sqlite3', echo=True)
        self.sess = Session(self.engine)
        self.country_match_objects = self.sess.query(CountryMatch).all()
        self.ids = []
        self.matches = []
        self.sim_game_class = SimGame()
        self.order = [[0], [2], [1], [3], [2], [1], [0], [3], [0], [1], [2], [3]]
        self.object_pair_list = []
        self.stage_id_counter = 0
        self.stage_id = 1
        self.change_num_list = [7,13,19,25,31]
        self.counter = 0

    def pairing(self, iterable):
        a = iter(iterable)
        return zip(a, a)
    """from stack overflow"""

    def pair_match_object(self, list_to_split):
        for a, b in self.pairing(list_to_split):
            self.matches.append([a, b])

    """from stack overflow"""

    def get_pair_list_of_objects(self):
        for group in self.list_of_groups:
            for i in range(len(self.order)):
                country_object = group[self.order[i][0]]
                self.object_pair_list.append(country_object)
        return self.object_pair_list

    def sim_the_game(self):
        self.get_pair_list_of_objects()
        self.pair_match_object(self.object_pair_list)
        for i, match in enumerate(self.matches):
            self.counter+=1
            self.stage_id_counter += 1
            self.match_number +=1
            if self.stage_id_counter % 6 == 0:
                self.stage_id += 1
                self.match_number = 1


            print(self.stage_id)
            result = self.sim_game_class.sim_game_object(match[0], match[1], self.stage_id, self.match_number)
            self.goals = result[1]
            self.update_table(match[0])
            self.goals = result[2]
            self.update_table(match[1])
            print(self.counter)


    def update_table(self, home_team):
        match_winner = self.sess.query(CountryMatch).filter_by(country_id=home_team.country_id).first()
        match_winner.score = self.goals
        match_winner.result = 0
        self.sess.commit()
        self.sess.close()

if __name__ == '__main__':
    gg = MakeMatches()
    print(gg.sim_the_game())
