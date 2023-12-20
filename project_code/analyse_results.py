from random import randint, sample
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import update

from project_code.models import Country, CountryMatch, Match


class Analyse:
    def __init__(self):
        self.average_goals_scored_overall = None
        self.highest_stage_id = 0
        self.num_of_ko_matches_played = 0
        self.ko_goals = 0
        self.num_of_group_matches_played = 0
        self.group_goals = 0
        self.num_of_matches_played = 0
        self.engine = create_engine('sqlite:///World_cup.sqlite3', echo=True)
        self.sess = Session(self.engine)
        self.goals = 0
        self.number_of_loses_dict = {'Argentina': 0, 'Australia': 0, 'Austria': 0, 'Belgium': 0, 'Canada': 0,
                                     'Croatia': 0, 'Czech Republic': 0, 'Denmark': 0,
                                     'England': 0, 'Finland': 0, 'France': 0, 'Germany': 0, 'Hungary': 0, 'Iceland': 0,
                                     'Ireland': 0, 'Italy': 0, 'Mexico': 0, 'Ghana': 0,
                                     'Netherlands': 0, 'Morocco': 0, 'Norway': 0, 'Poland': 0, 'Portugal': 0,
                                     'Romania': 0, 'Scotland': 0, 'Spain': 0, 'Sweden': 0, 'Ukraine': 0,
                                     'USA': 0, 'Wales': 0, 'Japan': 0, 'China': 0}
        self.number_of_wins_dict =  {'Argentina': 0, 'Australia': 0, 'Austria': 0, 'Belgium': 0, 'Canada': 0,
                                     'Croatia': 0, 'Czech Republic': 0, 'Denmark': 0,
                                     'England': 0, 'Finland': 0, 'France': 0, 'Germany': 0, 'Hungary': 0, 'Iceland': 0,
                                     'Ireland': 0, 'Italy': 0, 'Mexico': 0, 'Ghana': 0,
                                     'Netherlands': 0, 'Morocco': 0, 'Norway': 0, 'Poland': 0, 'Portugal': 0,
                                     'Romania': 0, 'Scotland': 0, 'Spain': 0, 'Sweden': 0, 'Ukraine': 0,
                                     'USA': 0, 'Wales': 0, 'Japan': 0, 'China': 0}

    def controller(self, country_name):
        self.country_object = self.sess.query(Country).filter_by(country_name=country_name).first()
        self.get_all_basic_stats()

    def get_all_basic_stats(self):
        self.get_all_goals_and_games_played()
        self.get_all_group_stage_goals_and_num_of_matches_played()
        self.get_all_ko_goals_and_num_of_matches_played()
        self.get_country_they_lost_or_won_to_most(self.number_of_loses_dict, 'loss')
        self.get_country_they_lost_or_won_to_most(self.number_of_wins_dict, 'win')
        self.furthest_got_and_average_place()



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
                self.num_of_group_matches_played += 1
        '''Doesnt add match if they didnt score, but i will know how many games played in group as set number'''

    def get_all_ko_goals_and_num_of_matches_played(self):
        all_ko_games = self.sess.query(Match.match_id).filter(Match.stage_id > 8).all()
        for game in all_ko_games:
            goals = self.sess.query(CountryMatch.score).filter_by(match_id=game[0],
                                                                  country_id=self.country_object.country_id).first()
            if goals != None:
                self.ko_goals += goals[0]
                self.num_of_ko_matches_played += 1

    def get_country_they_lost_or_won_to_most(self, win_or_lose_dict, win_or_lose_var):
        all_games = self.sess.query(CountryMatch.match_id).filter_by(country_id=self.country_object.country_id).all()
        for match in all_games:
            opponent = self.sess.query(CountryMatch.country_id).filter_by(match_id=match[0]).all()
            if opponent[0][0] != self.country_object.country_id:
                result = self.sess.query(CountryMatch.result).filter_by(country_id=opponent[1][0],
                                                                        match_id=match[0]).first()
                if result[0] == win_or_lose_var:
                    country_name = self.sess.query(Country.country_name).filter_by(country_id=opponent[0][0]).first()
                    win_or_lose_dict[country_name[0]] += 1

            elif opponent[1][0] != self.country_object.country_id:
                result = self.sess.query(CountryMatch.result).filter_by(country_id=opponent[1][0],
                                                                        match_id=match[0]).first()
                if result[0] == win_or_lose_var:
                    country_name = self.sess.query(Country.country_name).filter_by(country_id=opponent[1][0]).first()
                    win_or_lose_dict[country_name[0]] += 1

    def furthest_got_and_average_place(self):

        all_games = self.sess.query(CountryMatch.match_id).filter_by(country_id=self.country_object.country_id).all()
        for match in all_games:
            stage = self.sess.query(Match.stage_id).filter_by(match_id = match[0]).first()
            if stage[0] > self.highest_stage_id:
                self.highest_stage_id = stage[0]
        '''Doesnt have average place'''








if __name__ == '__main__':
    ff = Analyse()
    print(ff.controller('England'))
