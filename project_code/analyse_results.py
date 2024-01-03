from random import randint, sample
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import update

from project_code.models import Country, CountryMatch, Match


class Analyse:
    def __init__(self):
        self.average_goals_scored_per_game_ko = None
        self.average_goals_scored_per_game_group = None
        self.average_goals_scored_per_game_overall = None
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
        self.number_of_wins_dict = {'Argentina': 0, 'Australia': 0, 'Austria': 0, 'Belgium': 0, 'Canada': 0,
                                    'Croatia': 0, 'Czech Republic': 0, 'Denmark': 0,
                                    'England': 0, 'Finland': 0, 'France': 0, 'Germany': 0, 'Hungary': 0, 'Iceland': 0,
                                    'Ireland': 0, 'Italy': 0, 'Mexico': 0, 'Ghana': 0,
                                    'Netherlands': 0, 'Morocco': 0, 'Norway': 0, 'Poland': 0, 'Portugal': 0,
                                    'Romania': 0, 'Scotland': 0, 'Spain': 0, 'Sweden': 0, 'Ukraine': 0,
                                    'USA': 0, 'Wales': 0, 'Japan': 0, 'China': 0}

    def controller(self, country_name):
        cn = country_name
        self.country_object = self.sess.query(Country).filter_by(country_name=cn).first()
        self.get_all_basic_stats()
        self.team_lost_to_most = max(self.number_of_loses_dict, key=self.number_of_loses_dict.get)
        self.team_beat_the_most = max(self.number_of_wins_dict, key=self.number_of_wins_dict.get)
        self.print_everything()

    def get_all_basic_stats(self):
        self.get_all_goals_and_games_played()
        self.get_all_group_stage_goals_and_num_of_matches_played()
        self.get_all_ko_goals_and_num_of_matches_played()
        self.get_country_they_lost_or_won_to_most(self.number_of_loses_dict, 'loss')
        self.get_country_they_lost_or_won_to_most(self.number_of_wins_dict, 'win')
        self.furthest_got_and_average_place()

        self.average_goals_conceded_group_or_ko()
        '''self.average_goals_conceded_ko = self.average_goals_conceded_group_or_ko('ko')'''
        self.average_goals_conceded()


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
            stage = self.sess.query(Match.stage_id).filter_by(match_id=match[0]).first()
            if stage[0] > self.highest_stage_id:
                self.highest_stage_id = stage[0]
        '''Doesnt have average place'''

    def average_goals_conceded(self):
        total = 0
        count = 0
        all_games = self.sess.query(CountryMatch.match_id).filter_by(country_id=self.country_object.country_id).all()
        for game in all_games:
            ids = self.sess.query(CountryMatch).filter_by(match_id=game[0]).all()
            if ids[0].country_id == self.country_object.country_id:
                goals = self.sess.query(CountryMatch.score).filter_by(match_id=game[0],
                                                                      country_id=ids[1].country_id).first()
            else:
                goals = self.sess.query(CountryMatch.score).filter_by(match_id=game[0],
                                                                      country_id=ids[0].country_id).first()
            total += goals[0]
            count += 1
        self.average_goals_conceded= total / count

    def average_goals_conceded_group_or_ko(self):
        count=0
        total=0
        all_games_country_match_object = self.sess.query(CountryMatch).filter_by(country_id=self.country_object.country_id).all()
        for cm in all_games_country_match_object:
            group=False
            match_id = cm.match_id
            sim_num = cm.simulation_number
            stage = self.sess.query(Match.stage_id).filter_by(match_id=match_id,simulation_number=sim_num).first()
            if stage[0] <9:
                group=True
                both_countries = self.sess.query(CountryMatch).filter_by(simulation_number=sim_num,match_id=match_id).all()
                if both_countries[0].country_id == self.country_object.country_id:
                    goals = self.sess.query(CountryMatch.score).filter_by(match_id=match_id,
                                                                          country_id=both_countries[1].country_id, simulation_number=sim_num).first()
                else:
                    goals = self.sess.query(CountryMatch.score).filter_by(match_id=match_id,
                                                                          country_id=both_countries[1].country_id,
                                                                          simulation_number=sim_num).first()
                total += goals[0]
                count += 1
        self.average_goals_conceded_in_group = total/count






    def print_everything(self):
        print(f'Average goals conceded overall: {self.average_goals_conceded}')
        print(f'Average goals conceded in the group: {self.average_goals_conceded_in_group}')
        '''print(f'Average goals conceded in the ko: {self.average_goals_conceded_ko}')'''
        print(f'Average goals scored overall: {self.goals/self.num_of_matches_played}')
        print(f'Average goals scored in the group: {self.group_goals / self.num_of_group_matches_played}')
        if self.num_of_ko_matches_played == 0:
            print(f'Average goals scored in the ko: 0')
        else:
            print(f'Average goals scored in the ko: {self.ko_goals / self.num_of_ko_matches_played}')
        print(f'The highest stage reached was: {self.highest_stage_id}')
        print(f'The country that they beat the most: {self.team_beat_the_most}')
        print(f'The country that they lost to the most: {self.team_lost_to_most}')


if __name__ == '__main__':
    ff = Analyse()
    print(ff.controller('England'))
