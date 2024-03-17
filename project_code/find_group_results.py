from random import randint, shuffle, sample, random

from numpy import random
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from project_code.run_group_matches import RunMatches
from project_code.models import Country, Match, CountryMatch, Stage
from project_code.create_group_matches import GroupGenerator


class FindGroupResults:
    def __init__(self):
        self.new_list_of_groups = []
        self.group_points = []
        self.all_points = []
        self.winner = None
        self.engine = create_engine('sqlite:///World_cup.sqlite3', echo=False)
        self.sess = Session(self.engine)
        self.countries = []
        self.group_generator = GroupGenerator()

        self.list_of_groups = []
        self.list_of_groups = self.group_generator.collate_groups()

        self.country_dict = {}
        self.came_first = []
        self.came_second = []

    def collective(self, sim_num):
        """
        collates of the functions being done

        Parameters
        ----------
        sim_num: This is the simulation number that the program is on

        Returns
        -------
        self.came_first: a list containing all the countries that came first in their group
        self.came_second: a list containing all the countries that came second in their group

        """

        self.get_all_countries()
        self.get_countries_points(sim_num)
        self.work_out_who_goes_through(sim_num)
        return self.came_first, self.came_second

    def get_all_countries(self):
        """
        gets all the country objects and adds them to a list

        Returns
        -------
        self.countries: a list of all the countries in the order of groups
        """

        for group in self.list_of_groups:
            for country in group:
                self.countries.append(country)
        return self.countries

    def get_countries_points(self, sim_num):
        """
        totals up the points that each country got and creates a list in the order that they are in the
        self.countries list

        Parameters
        ----------
        sim_num: This is the simulation number that the program is on

        Returns
        -------
        self.all_points: a list of all the points that each country has in each group
        """


        for country in self.countries:
            all_results = self.sess.query(CountryMatch.result).filter_by(country_id=country.country_id,
                                                                         simulation_number=sim_num).all()
            points = 0
            for result in all_results:
                result = result[0][0:]

                if result == 'win':
                    points += 3
                elif result == 'draw':
                    points += 1

            self.all_points.append(points)

        return self.all_points

    def work_out_who_goes_through(self, sim_num):
        """
        Goes through each group and works out who came first and second by calling the relevant methods

        Parameters
        ----------
        sim_num: This is the simulation number that the program is on

        Returns
        -------
        None
        """
        group_index = -1
        self.get_points_per_group(self.all_points)
        for group in self.group_points:
            print(f'the number of points that each country in the group has is {group}')
            group_index += 1
            self.highest_id = self.find_who_came_first(group, group_index, sim_num)
            self.find_who_came_second(group, group_index, sim_num)

    def get_points_per_group(self, list_to_split):
        """
        splits the list into a list of list with each smaller list being a group

        Parameters
        ----------
        list_to_split: a list of all the points that each country has in each group

        Returns
        -------
        None

        """
        for a, b, c, d in self.pairing(list_to_split):
            self.group_points.append([a, b, c, d])

    def pairing(self, iterable):
        '''DO'''
        a = iter(iterable)
        return zip(a, a, a, a)

    def find_who_came_first(self, group, group_index, sim_num):
        """
        Finds the country which came first by looking at points and goal difference if needed

        Parameters
        ----------
        group: List of the points that each country got in the group
        group_index: The index of the group within self.group_points
        sim_num: This is the simulation number that the program is on

        Returns
        -------
        highest_index: The index of the country that came first
        """
        mx = max(group)
        highest_index = group.index(max(group))
        group_list_minus_mx = group[:highest_index] + group[highest_index + 1:]
        if max(group_list_minus_mx) == mx:
            highest_index = self.get_highest_gd(group, group_index, mx, sim_num)

        print(f'the country that came first had the index of {highest_index}')
        self.came_first.append(self.list_of_groups[group_index][highest_index])
        return highest_index

    def find_who_came_second(self, group, group_index, sim_num):
        """
        Finds the country which came second by looking at points and goal difference if needed

        Parameters
        ----------
        group: List of the points that each country got in the group
        group_index: The index of the group within self.group_points
        sim_num: This is the simulation number that the program is on

        Returns
        -------
        None
        """
        group.pop(self.highest_id)
        mx = max(group)
        highest_index = group.index(max(group))
        group_list_minus_mx = group[:highest_index] + group[highest_index + 1:]
        if max(group_list_minus_mx) == mx:
            highest_index = self.get_highest_gd(group, group_index, mx, sim_num)
            print(f'The country with the higher goal difference was the country with the index {highest_index}')
        if highest_index >= self.highest_id:
            highest_index += 1
        print(f'the country that came second had the index {highest_index}')
        self.came_second.append(self.list_of_groups[group_index][highest_index])

    def get_highest_gd(self, group, group_index, highest, sim_num):
        """
        This gets the country with the highest goal difference in the group

        Parameters
        ----------
        group: List of the points that each country got in the group
        group_index:The index of the group within self.group_points
        highest: The country with te initial highest points
        sim_num:This is the simulation number that the program is on

        Returns
        -------
        highest_index: The index of the country that had the highest gd
        """
        gd_list_i = []
        gd = self.get_goal_difference(group, group_index, sim_num)
        print(f'the list of goal difference is {gd}')
        for i, number in enumerate(group):
            if number == highest:
                gd_list_i.append(i)
        highest_index = max(gd_list_i)
        return highest_index

    def get_goal_difference(self, group, group_index, sim_num):
        """
        This gets the goal difference for each country in the group

        Parameters
        ----------
        group: This is the group that the program is analysis
        group_index: this is the index of the group within the list of groups
        sim_num: This is the simulation number that the program is on

        Returns
        -------
        gd_list: This is a list of each country's gd

        """
        gd_list = []
        gf = self.get_gf(group, group_index, sim_num)
        ga = self.get_ga(group, group_index, sim_num)

        for i in range(len(gf)):
            gd = gf[i] - ga[i]
            gd_list.append(gd)

        return gd_list

    def get_gf(self, group, group_index, sim_num):
        """
        This compiles each country in the group's goals for

        Parameters
        ----------
        group: This is the group that the program is analysis
        group_index: this is the index of the group within the list of groups
        sim_num: This is the simulation number that the program is on

        Returns
        -------
        group_goals: This is a list of each country's goals for

        """
        group_goals = []
        for i, country in enumerate(group):
            country_object = self.list_of_groups[group_index][i]

            id = country_object.country_id
            goals = self.get_total_goals(id, sim_num)
            group_goals.append(goals)
        return group_goals

    def get_total_goals(self, id, sim_num):
        """
        This gets a countries goals that they scored in the group
        Parameters
        ----------
        id: This is the id of the country it is looking at
        sim_num: This is the simulation number that the program is on

        Returns
        -------
        total_goals: This is the goals for that the country has

        """
        total_goals = 0
        all_goals = self.sess.query(CountryMatch.score).filter_by(country_id=id, simulation_number=sim_num).all()

        for goals in all_goals:
            goals = str(goals[0])
            goals = int(goals)
            total_goals += goals
        return total_goals

    def get_ga(self, group, group_index, sim_num):
        """
        This compiles each country in the group's goals against

        Parameters
        ----------
        group: This is the group that the program is analysis
        group_index: this is the index of the group within the list of groups
        sim_num: This is the simulation number that the program is on

        Returns
        -------
        group_conceded: This is a list of each country's goals against
        """
        group_conceded = []
        for i, country in enumerate(group):
            country_object = self.list_of_groups[group_index][i]

            id = country_object.country_id
            goals = self.get_total_goals_conceded(id, sim_num)
            group_conceded.append(goals)
        return group_conceded

    def get_total_goals_conceded(self, id, sim_num):
        """
        This gets a countries goals that they conceded in the group
        Parameters
        ----------
        id: This is the id of the country it is looking at
        sim_num: This is the simulation number that the program is on

        Returns
        -------
        total_conceded: This is the goals against that the country has

        """
        total_conceded = 0
        all_games = self.sess.query(CountryMatch.match_id).filter_by(country_id=id, simulation_number=sim_num).all()
        for game in all_games:
            ids = self.sess.query(CountryMatch).filter_by(match_id=game[0]).all()
            if ids[0].country_id == id:
                goals = self.sess.query(CountryMatch.score).filter_by(match_id=game[0],
                                                                      country_id=ids[1].country_id).first()
            else:
                goals = self.sess.query(CountryMatch.score).filter_by(match_id=game[0],
                                                                      country_id=ids[0].country_id).first()
            total_conceded += goals[0]

        return total_conceded


if __name__ == '__main__':
    gg = FindGroupResults()
    print(gg.collective(1))
