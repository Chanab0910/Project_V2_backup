from random import randint, shuffle, sample, random

from numpy import random
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from run_group_matches import MakeMatches
from project_code.models import Country, Match, CountryMatch, Stage
from project_code.create_group_matches import GroupGenerator

'''Could go through each row in match and check if they are certain group. Then create list of points for each group'''


class FindGroupResults:
    def __init__(self):
        self.group_points = []
        self.all_points = []
        self.winner = None
        self.engine = create_engine('sqlite:///World_cup.sqlite3', echo=True)
        self.sess = Session(self.engine)
        self.countries = []
        self.group_generator = GroupGenerator()
        self.mm = MakeMatches()
        self.list_of_groups = []
        self.list_of_groups = self.group_generator.collate_groups()
        self.country_dict = {}
        self.came_first = []
        self.came_second = []

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

    def work_out_who_goes_through(self):
        highest = 0
        second = 0

        group_index = -1
        self.pair_match_object(self.all_points)
        for group in self.group_points:
            same = False
            group_index += 1
            highest_index = group.index(max(group))
            mx = max(group)
            group_list_minus_mx = group[:highest_index] + group[highest_index + 1:]
            if max(group_list_minus_mx) == mx:
                same = True
            if same:
                list_of_ga = self.get_GA(group, group_index)
                list_of_gc = self.get_GC(group, group_index)
                highest_index = self.find_highest_ga(list_of_ga,list_of_gc, 'first')
            country_index = highest_index
            self.came_first.append(self.list_of_groups[group_index][country_index])

            same = False
            group.pop(highest_index)
            second_max = max(group_list_minus_mx)
            second_index = group.index(max(group_list_minus_mx))
            if second_index >= highest_index:
                second_index+=1
            group_list_minus_second = group_list_minus_mx[:second_index] + group_list_minus_mx[second_index + 1:]
            if max(group_list_minus_second) == second_max:
                same = True
            if same:
                list_of_ga = self.get_GA(group_list_minus_mx, group_index)
                list_of_gc = self.get_GC(group_list_minus_mx, group_index)
                second_index = self.find_highest_ga(list_of_ga,list_of_gc, 'second')
            country_index = second_index
            self.came_second.append(self.list_of_groups[group_index][country_index])


    def get_GA(self, group, group_index):
        group_goals = []
        for i, country in enumerate(group):
            country_object = self.list_of_groups[group_index][i]

            id = country_object.country_id
            goals = self.get_total_goals(id)
            group_goals.append(goals)
        return group_goals

    def get_GC(self, group, group_index):
        group_conceded = []
        for i, country in enumerate(group):
            country_object = self.list_of_groups[group_index][i]

            id = country_object.country_id
            goals = self.get_total_goals_conceded(id)
            group_conceded.append(goals)
        return group_conceded

    def find_highest_ga(self, list_of_ga,list_of_gc, f_or_s):
        highest_id = 0
        highest = 0
        second_id = 0
        second = 0
        for i, score in enumerate(list_of_ga):
            gd = score - list_of_gc[i]
            if gd > highest:
                second = highest
                highest = score
                highest_id = i
            elif gd > second:
                second = score
                second_id = i
        if f_or_s == 'first':
            return highest_id
        else:
            return second_id

    def get_total_goals(self, id):
        total_goals = 0
        all_goals = self.sess.query(CountryMatch.score).filter_by(country_id=id).all()

        for goals in all_goals:
            goals = str(goals[0])
            goals = int(goals)
            total_goals += goals
        return total_goals

    def get_total_goals_conceded(self,id):
        total = 0

        all_games = self.sess.query(CountryMatch.match_id).filter_by(country_id=id).all()
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

    def pairing(self, iterable):
        a = iter(iterable)
        return zip(a, a, a, a)

    """from stack overflow"""

    def pair_match_object(self, list_to_split):
        for a, b, c, d in self.pairing(list_to_split):
            self.group_points.append([a, b, c, d])

    def collective(self,sim_num):
        """collates of the functions being done"""

        self.get_all_countries()
        self.get_countries_points(sim_num)
        self.work_out_who_goes_through()
        return self.came_first, self.came_second



if __name__ == '__main__':
    gg = FindGroupResults()
    print(gg.collective(i))