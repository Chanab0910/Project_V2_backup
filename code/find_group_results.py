from random import randint, shuffle, sample, random

from numpy import random
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from code.models import Country, Match, CountryMatch, Stage
from code.create_groups import GroupGenerator


class FindGroupResults:
    def __init__(self):
        self.all_points = []
        self.winner = None
        self.engine = create_engine('sqlite:///World_cup.sqlite3', echo=True)
        self.sess = Session(self.engine)
        self.countries = []
        self.group_generator = GroupGenerator()
        self.list_of_groups = []
        self.list_of_groups = self.group_generator.collate_groups()

    def get_all_countries(self):
        """gets all the country objects and adds them to a list"""
        self.countries = self.sess.query(Country).all()
        return self.countries

    def get_countries_points(self):
        """totals up the points that each country got and creates a list in the order that they are in the Country
        table"""
        for country in self.countries:
            all_results = self.sess.query(CountryMatch.result).filter_by(country_id=country.country_id).all()
            points = 0
            for result in all_results:
                result = str(result)[2:-3]
                result = int(result)
                points += result

            self.all_points.append(points)
            print(self.all_points)
        return self.all_points

    def work_out_who_goes_through(self):
        ...

    def collective(self):
        """collates of the functions being done"""
        self.get_all_countries()
        self.get_countries_points()


if __name__ == '__main__':
    gg = FindGroupResults()
    print(gg.collective())
