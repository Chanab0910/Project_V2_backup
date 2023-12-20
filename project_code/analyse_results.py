from random import randint, sample
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import update

from project_code.models import Country, CountryMatch, Match


class Analyse:
    def __init__(self):
        self.num_of_ko_matches_played = 0
        self.ko_goals = 0
        self.num_of_group_matches_played = 0
        self.group_goals = 0
        self.num_of_matches_played = 0
        self.engine = create_engine('sqlite:///World_cup.sqlite3', echo=True)
        self.sess = Session(self.engine)
        self.goals = 0

    def controller(self, country_name):
        self.country_object = self.sess.query(Country).filter_by(country_name=country_name).first()
        self.get_all_basic_stats()

    def get_all_basic_stats(self):
        self.get_all_goals_and_games_played()
        self.get_all_group_stage_goals_and_num_of_matches_played()
        self.get_all_ko_goals_and_num_of_matches_played()

    def get_all_goals_and_games_played(self):
        goals_list = self.sess.query(CountryMatch.score).filter_by(country_id=self.country_object.country_id).all()
        for goals in goals_list:
            self.goals += goals[0]
            self.num_of_matches_played += 1

    def get_all_group_stage_goals_and_num_of_matches_played(self):
        all_group_games = self.sess.query(Match.match_id).filter(Match.stage_id < 9).all()
        for game in all_group_games:
            goals = self.sess.query(CountryMatch.score).filter_by(match_id=game[0],
                                                                  country_id=self.country_object.country_id).first()
            if goals != None:
                self.group_goals += goals[0]
                self.num_of_group_matches_played +=1
        '''Doesnt add match if they didnt score, but i will know how many games played in group as set number'''
        
    def get_all_ko_goals_and_num_of_matches_played(self):
        all_ko_games = self.sess.query(Match.match_id).filter(Match.stage_id > 8).all()
        for game in all_ko_games:
            goals = self.sess.query(CountryMatch.score).filter_by(match_id=game[0],
                                                                  country_id=self.country_object.country_id).first()
            if goals != None:
                self.ko_goals += goals[0]
                self.num_of_ko_matches_played +=1
    '''Not got all the match table entries'''

if __name__ == '__main__':
    ff = Analyse()
    print(ff.controller('Ghana'))
