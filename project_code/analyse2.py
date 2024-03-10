from random import randint, sample
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import update
from project_code.models import Country, CountryMatch, Match, Stage
from project_code.redo_find_group_results import FindGroupResults

engine = create_engine('sqlite:///../project_code/World_cup.sqlite3', echo=True)
sess = Session(engine)

class Analyse:
    def __init__(self):
        self.number_of_wc_wins = 0
        self.average_goals_scored_per_game_ko = None
        self.average_goals_scored_per_game_group = None
        self.average_goals_scored_per_game_overall = None
        self.fgr = FindGroupResults
        self.all_countries = self.fgr.get_all_countries
        self.highest_stage_id = 0
        self.num_of_ko_matches_played = 0
        self.ko_goals = 0
        self.num_of_group_matches_played = 0
        self.group_goals = 0
        self.num_of_matches_played = 0
        self.engine = create_engine('sqlite:///../project_code/World_cup.sqlite3', echo=True)
        self.sess = Session(self.engine)
        self.goals = 0
        self.number_of_loses_dict = {'Argentina': 0, 'France': 0, 'England': 0, 'Belgium': 0, 'Brazil': 0,
                                     'Netherlands': 0, 'Portugal': 0, 'Spain': 0,
                                     'Italy': 0, 'Croatia': 0, 'Uruguay': 0, 'Morocco': 0, 'USA': 0, 'Columbia': 0,
                                     'Mexico': 0, 'Germany': 0, 'Senegal': 0, 'Japan': 0,
                                     'Switzerland': 0, 'Iran': 0, 'Denmark': 0, 'Korea': 0, 'Australia': 0,
                                     'Ukraine': 0, 'Austria': 0, 'Sweden': 0, 'Hungary': 0, 'Nigeria': 0,
                                     'Wales': 0, 'Poland': 0, 'Equador': 0, 'Serbia': 0}
        self.number_of_wins_dict = {'Argentina': 0, 'France': 0, 'England': 0, 'Belgium': 0, 'Brazil': 0,
                                     'Netherlands': 0, 'Portugal': 0, 'Spain': 0,
                                     'Italy': 0, 'Croatia': 0, 'Uruguay': 0, 'Morocco': 0, 'USA': 0, 'Columbia': 0,
                                     'Mexico': 0, 'Germany': 0, 'Senegal': 0, 'Japan': 0,
                                     'Switzerland': 0, 'Iran': 0, 'Denmark': 0, 'Korea': 0, 'Australia': 0,
                                     'Ukraine': 0, 'Austria': 0, 'Sweden': 0, 'Hungary': 0, 'Nigeria': 0,
                                     'Wales': 0, 'Poland': 0, 'Equador': 0, 'Serbia': 0}

        self.dict_of_where_they_came = {'Group': 0, 'Round of 16': 0, 'Quarter-final': 0, 'Semi-final': 0, 'Final': 0,
                                        'Win': 0}

        self.number_of_times_played_dict = {'Argentina': 0, 'France': 0, 'England': 0, 'Belgium': 0, 'Brazil': 0,
                                     'Netherlands': 0, 'Portugal': 0, 'Spain': 0,
                                     'Italy': 0, 'Croatia': 0, 'Uruguay': 0, 'Morocco': 0, 'USA': 0, 'Columbia': 0,
                                     'Mexico': 0, 'Germany': 0, 'Senegal': 0, 'Japan': 0,
                                     'Switzerland': 0, 'Iran': 0, 'Denmark': 0, 'Korea': 0, 'Australia': 0,
                                     'Ukraine': 0, 'Austria': 0, 'Sweden': 0, 'Hungary': 0, 'Nigeria': 0,
                                     'Wales': 0, 'Poland': 0, 'Equador': 0, 'Serbia': 0}



    def controller(self, country_name):
        # This is the method that calls everything and is called by other methods to get all of the data about the country
        cn = str(country_name)
        self.country_object = self.sess.query(Country).filter_by(country_name=cn).first()
        self.all_games_played = self.sess.query(CountryMatch).filter_by(
            country_id=self.country_object.country_id).all()

        self.all_ko_games = self.sess.query(Match.match_id).filter(Match.stage_id > 8).all()
        self.get_all_basic_stats(country_name)

        '''self.print_everything()'''
        '''return self.average_goals_conceded, self.average_goals_conceded_in_group, self.average_goals_conceded_in_ko, self.average_goals, self.average_goals_group, self.average_goals_ko, \
               self.highest_stage, self.dict_of_where_they_came, self.team_beat_the_most, self.team_they_beat_the_highest_percentage_of_times, self.team_lost_to_most, self.team_they_lost_to_the_highest_percentage_of_times, self.percentage_get_to_dict
'''
    def get_all_basic_stats(self, country_name):
        self.get_all_goals_and_games_played()


    def get_all_goals_and_games_played(self):
        for game in self.all_games_played:
            goals = game.score
            self.goals += goals[0]
            self.num_of_matches_played += 1
        return self.goals / self.num_of_matches_played

    def get_all_group_stage_goals_and_num_of_matches_played(self):
        all_group_games = self.sess.query(Match.match_id).filter(Match.stage_id < 9).all()
        for game in all_group_games:
            goals = self.sess.query(CountryMatch.score).filter_by(match_id=game[0],
                                                                  country_id=self.country_object.country_id).first()
            self.group_goals += goals[0]
            self.num_of_group_matches_played += 1
