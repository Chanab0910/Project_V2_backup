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
        self.list_of_obj = self.mm.get_loo()
        self.country_dict = {}
        self.came_first = []
        self.came_second = []

    def get_all_countries(self):
        """gets all the country objects and adds them to a list"""
        print(self.list_of_groups)
        for group in self.list_of_groups:
            for country in group:
                self.countries.append(country)
        return self.countries

    def get_countries_points(self):
        """totals up the points that each country got and creates a list in the order that they are in the Country
        table"""

        for country in self.countries:
            all_results = self.sess.query(CountryMatch.result).filter_by(country_id=country.country_id).all()
            points = 0

            for result in all_results:
                result = result[0][0:]

                if result == 'win':
                    points += 3
                elif result == 'draw':
                    points += 1

            self.all_points.append(points)
        print(self.all_points)
        return self.all_points

    def work_out_who_goes_through(self):
        highest = 0
        second = 0
        same = False
        group_index = -1
        country_index = -1
        self.pair_match_object(self.all_points)
        for group in self.group_points:
            group_index +=1
            for country in group:
                country_index +=1
                if country > highest:
                    highest = country
                    same = False
                if country == highest:
                    same = True
            if same == True:
                self.check_GA()
            else:
                self.came_first.append(self.list_of_groups[group_index][country_index])



    def check_GA(self):
        ...

    def pairing(self, iterable):
        a = iter(iterable)
        return zip(a, a,a,a)

    """from stack overflow"""

    def pair_match_object(self, list_to_split):
        for a, b,c,d in self.pairing(list_to_split):
            self.group_points.append([a, b,c,d])

    def collective(self):
        """collates of the functions being done"""

        self.get_all_countries()
        self.get_countries_points()
        self.work_out_who_goes_through()


if __name__ == '__main__':
    gg = FindGroupResults()
    print(gg.collective())
