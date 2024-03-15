"""
This is used to loop through all the entries in country_match and put them through simulate_game
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import update
from project_code.sim_game import SimGame
from project_code.create_group_matches import GroupGenerator
from project_code.models import Country, CountryMatch
import sqlite3


class RunMatches:
    def __init__(self):
        self.list = []
        self.match_id_lists = [x for x in range(49)]
        self.match_number = 0
        self.score = []

        self.group_generator = GroupGenerator()
        self.list_of_groups = []
        self.list_of_groups = self.group_generator.collated_groups
        self.engine = create_engine('sqlite:///World_cup.sqlite3', echo=False)
        self.sess = Session(self.engine)

        self.list_of_objects = []
        self.ids = []
        self.matches = []
        self.sim_game_class = SimGame()
        self.order = [[0], [2], [1], [3], [2], [1], [0], [3], [0], [1], [2], [3]]
        self.object_pair_list = []
        self.stage_id_counter = -1
        self.stage_id = 0
        self.change_num_list = [7, 13, 19, 25, 31]
        self.counter = 0

    def pairing(self, iterable):
        a = iter(iterable)
        return zip(a, a)

    """from stack overflow"""

    def pair_match_object(self, list_to_split):
        for thing1, thing2 in self.pairing(list_to_split):
            self.matches.append([thing1, thing2])

    """from stack overflow"""

    def get_list_of_objects(self, sim_num):
        """
        Gets a list of the country objects by going through each CountryMatch row and appending the object to the list.

        Parameters
        ----------
        sim_num: This is the simulation number that the program is on

        Returns ------- self.list_of_objects: This gives the program a list of objects in the order of the matches
        and what countries are in them.

        """
        self.country_match_ids = self.sess.query(CountryMatch.country_id).filter_by(simulation_number=sim_num).all()
        for ids in self.country_match_ids:
            object = self.sess.get(Country, ids)
            self.list_of_objects.append(object)
        return self.list_of_objects

    def sim_the_game(self, sim_num):
        """
        This loops though each game and calls the relevant methods to simulate it. It then gets the result and score and calls the update_table method.

        Parameters
        ----------
        sim_num: This is the simulation number that the program is on

        Returns
        -------
        None
        """
        match_id = 0
        self.get_list_of_objects(sim_num)
        self.pair_match_object(self.list_of_objects)
        for i, match in enumerate(self.matches):
            match_id += 1
            self.counter += 1
            self.stage_id_counter += 1
            self.match_number += 1
            if self.stage_id_counter % 6 == 0:
                self.stage_id += 1
                self.match_number = 1

            result = self.sim_game_class.sim_game_object(match[0], match[1], self.stage_id, self.match_number, sim_num,
                                                         match_id)
            print(result)
            self.score.append(result[1])
            self.score.append(result[2])

            self.update_table(sim_num)
            self.score = []

            if self.match_number == 63:
                self.match_number = 0




    def update_table(self, sim_num):
        """
        This updates the CountryMatch table based on the results of each game

        Parameters
        ----------
        sim_num: This is the simulation number that the program is on

        Returns
        -------
        None
        """

        match_id = self.match_id_lists[self.counter]
        country_matches = self.sess.query(CountryMatch).filter_by(match_id=match_id, simulation_number=sim_num).all()
        country_matches[0].score = self.score[0]
        country_matches[1].score = self.score[1]
        if self.score[0] > self.score[1]:
            country_matches[0].result = 'win'
            country_matches[1].result = 'loss'
        elif self.score[1] > self.score[0]:
            country_matches[0].result = 'loss'
            country_matches[1].result = 'win'
        else:
            country_matches[0].result = 'draw'
            country_matches[1].result = 'draw'

        self.sess.commit()






if __name__ == '__main__':
    gg = RunMatches()
    print(gg.sim_the_game(1))
