from random import randint, sample
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import update
from sim_game import SimGame
from project_code.models import Country, CountryMatch


class Analyse:
    def __init__(self):
        self.engine = create_engine('sqlite:///World_cup.sqlite3', echo=True)
        self.sess = Session(self.engine)
        self.goals = 0

    def controller(self, country_name):
        country_object = self.sess.query(Country).filter_by(country_name=country_name)
        self.ids = country_object.id
        self.get_all_basic_stats(country_object)

    def get_all_basic_stats(self, country_object):
        self.get_all_goals(country_object)

    def get_all_goals(self, country_object):
        goals_list = self.sess.query(CountryMatch.score).filter_by(country_id=country_object.id)
        for goals in goals_list:
            ...


if __name__ == '__main__':
    ff = Analyse()
    print(ff.controller('England'))
