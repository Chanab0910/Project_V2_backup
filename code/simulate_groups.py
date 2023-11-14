from random import randint, shuffle, sample, random

from numpy import random
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from code.models import Country
from create_groups import GroupGenerator
from sim_game import SimGame

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
        self.sim_game_class = SimGame()

    def groups_matches(self):
        # Takes each group and simulates it using sim_game and iterating through each game in the group
        for group in self.list_of_groups:
            self.group_id += 1

            for i in range(len(self.order)-1):
                print(self.sim_game_class.sim_game_object(group[self.order[i - 1][0]], group[self.order[i - 1][1]]))
                #self.sim_game_object(group[self.order[i - 1][0]], group[self.order[i - 1][1]])


if __name__ == '__main__':
    gg = SimulateGroups()
    print(gg.groups_matches())
