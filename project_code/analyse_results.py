from random import randint, sample
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import update

from project_code.models import Country, CountryMatch, Match, Stage
from project_code.redo_find_group_results import FindGroupResults


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

        self.dict_of_where_they_came = {'Group': 0, 'Round of 16': 0, 'Quarter-final': 0, 'Semi-final': 0, 'Final': 0}

        self.number_of_times_played_dict = {'Argentina': 0, 'Australia': 0, 'Austria': 0, 'Belgium': 0, 'Canada': 0,
                                            'Croatia': 0, 'Czech Republic': 0, 'Denmark': 0,
                                            'England': 0, 'Finland': 0, 'France': 0, 'Germany': 0, 'Hungary': 0,
                                            'Iceland': 0,
                                            'Ireland': 0, 'Italy': 0, 'Mexico': 0, 'Ghana': 0,
                                            'Netherlands': 0, 'Morocco': 0, 'Norway': 0, 'Poland': 0, 'Portugal': 0,
                                            'Romania': 0, 'Scotland': 0, 'Spain': 0, 'Sweden': 0, 'Ukraine': 0,
                                            'USA': 0, 'Wales': 0, 'Japan': 0, 'China': 0}

    def controller(self, country_name):
        cn = country_name
        self.country_object = self.sess.query(Country).filter_by(country_name=cn).first()
        self.get_all_basic_stats()

        self.print_everything()

    def get_all_basic_stats(self):
        self.get_all_goals_and_games_played()
        self.get_all_group_stage_goals_and_num_of_matches_played()
        self.get_all_ko_goals_and_num_of_matches_played()
        self.get_country_they_lost_or_won_to_most()
        self.furthest_got_and_average_place()
        self.average_goals_conceded_group_or_ko()
        self.average_goals_conceded()
        self.team_lost_to_most = max(self.number_of_loses_dict, key=self.number_of_loses_dict.get)
        self.team_beat_the_most = max(self.number_of_wins_dict, key=self.number_of_wins_dict.get)
        self.get_number_of_times_they_played_each_country()
        self.team_they_beat_and_lost_to_the_most_percentage()
        self.number_of_wins()

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

    def get_country_they_lost_or_won_to_most(self):
        all_games_played = self.sess.query(CountryMatch).filter_by(country_id=self.country_object.country_id).all()

        for game in all_games_played:
            match = self.sess.query(CountryMatch).filter_by(match_id=game.match_id,
                                                            simulation_number=game.simulation_number).all()
            if match[0].country_id == self.country_object.country_id:
                opposition = match[1]
            else:
                opposition = match[0]

            if opposition.result == 'loss':
                country_name = self.sess.query(Country.country_name).filter_by(country_id=opposition.country_id).first()
                self.number_of_wins_dict[country_name[0]] +=1

            if opposition.result == 'win':
                country_name = self.sess.query(Country.country_name).filter_by(country_id=opposition.country_id).first()
                self.number_of_loses_dict[country_name[0]] +=1

    def furthest_got_and_average_place(self):

        for i in range(1, 100):

            highest_in_sim = 0
            all_games_in_sim = self.sess.query(CountryMatch.match_id).filter_by(
                country_id=self.country_object.country_id, simulation_number=i).all()
            for match in all_games_in_sim:
                stage = self.sess.query(Match.stage_id).filter_by(match_id=match[0]).first()
                if stage[0] > self.highest_stage_id:
                    self.highest_stage_id = stage[0]
                if stage[0] > highest_in_sim:
                    highest_in_sim = stage[0]

            if highest_in_sim < 9:
                self.dict_of_where_they_came['Group'] += 1
            elif 8 < highest_in_sim < 17:
                self.dict_of_where_they_came['Round of 16'] += 1
            elif 16 < highest_in_sim < 21:
                self.dict_of_where_they_came['Quarter-final'] += 1
            elif highest_in_sim == 21 or highest_in_sim == 22:
                self.dict_of_where_they_came['Semi-final'] += 1
            elif highest_in_sim == 23:
                self.dict_of_where_they_came['Final'] += 1

        self.highest_stage = self.sess.query(Stage.level).filter_by(stage_id=self.highest_stage_id).first()
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
        self.average_goals_conceded = total / count

    def average_goals_conceded_group_or_ko(self):
        group_count = 0
        group_total = 0
        ko_count = 0
        ko_total = 0
        all_games_country_match_object = self.sess.query(CountryMatch).filter_by(
            country_id=self.country_object.country_id).all()
        for cm in all_games_country_match_object:
            match_id = cm.match_id
            sim_num = cm.simulation_number
            stage = self.sess.query(Match.stage_id).filter_by(match_id=match_id, simulation_number=sim_num).first()

            if stage[0] < 9:
                both_countries = self.sess.query(CountryMatch).filter_by(simulation_number=sim_num,
                                                                         match_id=match_id).all()
                if both_countries[0].country_id == self.country_object.country_id:
                    goals = self.sess.query(CountryMatch.score).filter_by(match_id=match_id,
                                                                          country_id=both_countries[1].country_id,
                                                                          simulation_number=sim_num).first()
                else:
                    goals = self.sess.query(CountryMatch.score).filter_by(match_id=match_id,
                                                                          country_id=both_countries[1].country_id,
                                                                          simulation_number=sim_num).first()
                group_total += goals[0]
                group_count += 1
            else:
                both_countries = self.sess.query(CountryMatch).filter_by(simulation_number=sim_num,
                                                                         match_id=match_id).all()
                if both_countries[0].country_id == self.country_object.country_id:
                    goals = self.sess.query(CountryMatch.score).filter_by(match_id=match_id,
                                                                          country_id=both_countries[1].country_id,
                                                                          simulation_number=sim_num).first()
                else:
                    goals = self.sess.query(CountryMatch.score).filter_by(match_id=match_id,
                                                                          country_id=both_countries[1].country_id,
                                                                          simulation_number=sim_num).first()
                ko_total += goals[0]
                ko_count += 1
        self.average_goals_conceded_in_group = group_total / group_count
        self.average_goals_conceded_in_ko = ko_total / ko_count

    def number_of_wins(self):
        for i in range(1, 100):
            all_games_in_sim = self.sess.query(CountryMatch.match_id).filter_by(
                country_id=self.country_object.country_id, simulation_number=i).all()
            for match in all_games_in_sim:
                stage = self.sess.query(Match.stage_id).filter_by(match_id=match[0], simulation_number=i).first()

                if stage[0] == 23:
                    result = self.sess.query(CountryMatch.result).filter_by(match_id=match[0], simulation_number=i,
                                                                            country_id=self.country_object.country_id).first()
                    if result[0] == 'win':
                        self.number_of_wc_wins += 1

    def get_number_of_times_they_played_each_country(self):
        all_games_played = self.sess.query(CountryMatch).filter_by(country_id=self.country_object.country_id).all()

        for game in all_games_played:
            match = self.sess.query(CountryMatch).filter_by(match_id=game.match_id,
                                                            simulation_number=game.simulation_number).all()
            if match[0].country_id == self.country_object.country_id:
                opposition = match[1]
            else:
                opposition = match[0]

            country_name = self.sess.query(Country.country_name).filter_by(country_id=opposition.country_id).first()
            self.number_of_times_played_dict[country_name[0]] += 1

    def team_they_beat_and_lost_to_the_most_percentage(self):
        list_of_countries = ['Argentina', 'Australia', 'Austria', 'Belgium', 'Canada', 'Croatia', 'Czech Republic',
                             'Denmark', 'England', 'Finland', 'France', 'Germany',
                             'Hungary', 'Iceland', 'Ireland', 'Italy', 'Mexico', 'Ghana', 'Netherlands', 'Morocco',
                             'Norway', 'Poland', 'Portugal', 'Romania', 'Scotland', 'Spain',
                             'Sweden', 'Ukraine', 'USA', 'Wales', 'Japan', 'China'
                             ]
        percentage_list_won = []
        percentage_list_lost=[]
        for country in list_of_countries:
            number_won = self.number_of_wins_dict[country]
            number_lost = self.number_of_loses_dict[country]
            number_played = self.number_of_times_played_dict[country]
            try:
                percentage_won = number_won/number_played
            except:
                percentage_won = 0
            try:
                percentage_lost = number_lost/number_played
            except:
                percentage_lost = 0
            percentage_list_won.append(percentage_won)
            percentage_list_lost.append(percentage_lost)

        self.team_they_beat_the_highest_percentage_of_times = list_of_countries[percentage_list_won.index(max(percentage_list_won))]
        self.team_they_lost_to_the_highest_percentage_of_times = list_of_countries[percentage_list_lost.index(max(percentage_list_lost))]

        '''Doesnt quite work yet'''

    def print_everything(self):
        print(f'Average goals conceded per match overall: {self.average_goals_conceded:.2f}')
        print(f'Average goals conceded in the group per match: {self.average_goals_conceded_in_group:.2f}')
        print(f'Average goals conceded in the ko per match: {self.average_goals_conceded_in_ko:.2f}')
        print(f'Average goals scored per match overall: {self.goals / self.num_of_matches_played:.2f}')
        print(f'Average goals scored in the group per match: {self.group_goals / self.num_of_group_matches_played:.2f}')
        try:
            print(f'Average goals scored in the ko per match: {self.ko_goals / self.num_of_ko_matches_played:.2f}')
        except:
            print(f'Average goals scored in the ko per match: 0')
        print(f'The highest stage reached was: {self.highest_stage[0]}')
        print(
            f"{self.country_object.country_name} got knocked out in: The Groups {self.dict_of_where_they_came['Group']} times")
        print(f"                              The Round of 16 {self.dict_of_where_they_came['Round of 16']} times")
        print(f"                              The Quarter-Finals {self.dict_of_where_they_came['Quarter-final']} times")
        print(f"                              The Semi-Finals {self.dict_of_where_they_came['Semi-final']} times")
        print(f"                              The Final {self.dict_of_where_they_came['Final']} times")
        print(f'Number of times they won the World Cup: {self.number_of_wc_wins}')
        print(f'The country that they beat the most number of times was {self.team_beat_the_most}, but they beat {self.team_they_beat_the_highest_percentage_of_times} with the highest percentage win rate')
        print(f'The country that they lost to the most was {self.team_lost_to_most}, but they lost to {self.team_they_lost_to_the_highest_percentage_of_times} with the highest percentage loss rate')


if __name__ == '__main__':
    ff = Analyse()
    print(ff.controller('England'))
