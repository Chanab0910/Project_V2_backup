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
        self.engine = create_engine('sqlite:///World_cup.sqlite3', echo=True)
        self.sess = Session(self.engine)
        self.countries = []
        self.group_generator = GroupGenerator()
        self.mm = RunMatches()
        self.list_of_groups = []
        self.list_of_groups = self.group_generator.collate_groups()

        self.country_dict = {}
        self.came_first = []
        self.came_second = []

    def collective(self,sim_num):
        """collates of the functions being done"""

        self.get_all_countries()
        self.get_countries_points(sim_num)
        self.work_out_who_goes_through(sim_num)
        return self.came_first,self.came_second

    def get_all_countries(self):
        """gets all the country objects and adds them to a list"""

        for group in self.list_of_groups:
            for country in group:
                self.countries.append(country)
        return self.countries

    def get_countries_points(self,sim_num):
        """totals up the points that each country got and creates a list in the order that they are in the Country
        table"""

        for country in self.countries:
            all_results = self.sess.query(CountryMatch.result).filter_by(country_id=country.country_id,simulation_number=sim_num).all()
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
        group_index = -1
        self.get_points_per_group(self.all_points)
        for group in self.group_points:
            group_index += 1
            self.highest_id = self.find_who_came_first(group, group_index, sim_num)
            self.find_who_came_second(group, group_index, sim_num)

    def get_points_per_group(self, list_to_split):
        for a, b, c, d in self.pairing(list_to_split):
            self.group_points.append([a, b, c, d])

    def pairing(self, iterable):
        a = iter(iterable)
        return zip(a, a, a, a)

    def find_who_came_first(self, group, group_index, sim_num):
        mx = max(group)
        highest_index = group.index(max(group))
        group_list_minus_mx = group[:highest_index] + group[highest_index + 1:]
        if max(group_list_minus_mx) == mx:
            highest_index = self.check_gd_for_first(group, group_index, mx, sim_num)

        self.came_first.append(self.list_of_groups[group_index][highest_index])
        return highest_index

    def find_who_came_second(self, group, group_index, sim_num ):
        group.pop(self.highest_id)
        mx = max(group)
        highest_index = group.index(max(group))
        group_list_minus_mx = group[:highest_index] + group[highest_index + 1:]
        if max(group_list_minus_mx) == mx:
            highest_index = self.check_gd_for_first(group, group_index, mx, sim_num)
        if highest_index >= self.highest_id:
            highest_index += 1
        self.came_second.append(self.list_of_groups[group_index][highest_index])

    def check_gd_for_first(self, group, group_index, highest, sim_num):
        gd_list_i = []
        gd = self.get_goal_difference(group, group_index, sim_num)
        for i, number in enumerate(group):
            if number == highest:
                gd_list_i.append(i)
        highest_index = max(gd_list_i)
        return highest_index

    def get_goal_difference(self, group, group_index, sim_num):
        gd_list = []
        gf = self.get_gf(group, group_index, sim_num)
        ga = self.get_ga(group, group_index, sim_num)

        for i in range(len(gf)):
            gd = gf[i] - ga[i]
            gd_list.append(gd)

        return gd_list

    def get_gf(self, group, group_index, sim_num):
        group_goals = []
        for i, country in enumerate(group):
            country_object = self.list_of_groups[group_index][i]

            id = country_object.country_id
            goals = self.get_total_goals(id, sim_num)
            group_goals.append(goals)
        return group_goals

    def get_total_goals(self, id, sim_num):
        total_goals = 0
        all_goals = self.sess.query(CountryMatch.score).filter_by(country_id=id, simulation_number = sim_num).all()

        for goals in all_goals:
            goals = str(goals[0])
            goals = int(goals)
            total_goals += goals
        return total_goals

    def get_ga(self, group, group_index, sim_num):
        group_conceded = []
        for i, country in enumerate(group):
            country_object = self.list_of_groups[group_index][i]

            id = country_object.country_id
            goals = self.get_total_goals_conceded(id, sim_num)
            group_conceded.append(goals)
        return group_conceded

    def get_total_goals_conceded(self, id, sim_num):
        total = 0

        all_games = self.sess.query(CountryMatch.match_id).filter_by(country_id=id, simulation_number = sim_num).all()
        for game in all_games:
            ids = self.sess.query(CountryMatch).filter_by(match_id=game[0]).all()
            if ids[0].country_id == id:
                goals = self.sess.query(CountryMatch.score).filter_by(match_id=game[0],
                                                                      country_id=ids[1].country_id).first()
            else:
                goals = self.sess.query(CountryMatch.score).filter_by(match_id=game[0],
                                                                      country_id=ids[0].country_id).first()
            total += goals[0]

        return total


if __name__ == '__main__':
    gg = FindGroupResults()
    print(gg.collective(1))
