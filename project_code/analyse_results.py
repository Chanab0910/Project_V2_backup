from random import randint, sample
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import update
from project_code.models import Country, CountryMatch, Match, Stage
from project_code.redo_find_group_results import FindGroupResults

engine = create_engine('sqlite:///../project_code/World_cup.sqlite3', echo=False)
sess = Session(engine)


class Analyse:
    '''descr
    attr
    methods'''
    def __init__(self):
        self.number_of_wc_wins = 0
        self.average_goals_scored_per_game_ko = None
        self.average_goals_scored_per_game_group = None
        self.average_goals_scored_per_game_overall = None
        self.fgr = FindGroupResults()
        self.all_countries = self.fgr.get_all_countries
        self.highest_stage_id = 0
        self.num_of_ko_matches_played = 0
        self.ko_goals = 0
        self.num_of_group_matches_played = 0
        self.group_goals = 0
        self.num_of_matches_played = 0
        self.engine = create_engine('sqlite:///../project_code/World_cup.sqlite3', echo=False)
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
                                            'Italy': 0, 'Croatia': 0, 'Uruguay': 0, 'Morocco': 0, 'USA': 0,
                                            'Columbia': 0,
                                            'Mexico': 0, 'Germany': 0, 'Senegal': 0, 'Japan': 0,
                                            'Switzerland': 0, 'Iran': 0, 'Denmark': 0, 'Korea': 0, 'Australia': 0,
                                            'Ukraine': 0, 'Austria': 0, 'Sweden': 0, 'Hungary': 0, 'Nigeria': 0,
                                            'Wales': 0, 'Poland': 0, 'Equador': 0, 'Serbia': 0}

    def controller(self, country_name):
        """This is the method that calls everything and is called by other methods to get all the data about the
        country """
        cn = str(country_name)
        self.country_object = self.sess.query(Country).filter_by(country_name=cn).first()
        self.get_all_basic_stats(country_name)

        '''self.print_everything()'''
        return self.average_goals_conceded, self.average_goals_conceded_in_group, self.average_goals_conceded_in_ko, self.average_goals, self.average_goals_group, self.average_goals_ko, \
            self.highest_stage, self.dict_of_where_they_came, self.team_beat_the_most, self.team_they_beat_the_highest_percentage_of_times, self.team_lost_to_most, self.team_they_lost_to_the_highest_percentage_of_times, self.percentage_get_to_dict

    def get_all_basic_stats(self, country_name):
        """
        calls the methods needed to get the basic data which can be manipulated later

        Parameters
        ----------
        country_name: name of the country

        Returns
        -------
        None
        """
        self.get_all_goals_and_games_played(country_name)
        self.get_all_group_stage_goals_and_num_of_matches_played()
        self.get_all_ko_goals_and_num_of_matches_played()
        self.get_country_they_lost_or_won_to_most()
        self.furthest_got_and_average_place(country_name)
        self.average_goals_conceded_group_or_ko()
        self.average_goals_conceded()
        self.team_lost_to_most = max(self.number_of_loses_dict, key=self.number_of_loses_dict.get)
        self.team_beat_the_most = max(self.number_of_wins_dict, key=self.number_of_wins_dict.get)
        self.get_number_of_times_they_played_each_country()
        self.team_they_beat_and_lost_to_the_most_percentage()
        self.average_goals = self.goals / self.num_of_matches_played
        self.average_goals_group = self.group_goals / self.num_of_group_matches_played
        self.average_goals_ko = self.ko_goals / self.num_of_ko_matches_played
        self.number_of_wins()

    def get_all_goals_and_games_played(self, country_name):
        """

        Parameters
        ----------
        country_name: name of the country

        Returns
        -------
        self.goals / self.num_of_matches_played: an expression which gives the average goals scored per game
        """
        # this queries all the goals scored in each match by a country. It then works out the total number of goals
        # by looping through each match and adding the goals to the total. At the same time it increments the number
        # of matches played which allows an average goals per game to be created
        self.country_object = self.sess.query(Country).filter_by(country_name=country_name).first()
        goals_list = self.sess.query(CountryMatch.score).filter_by(country_id=self.country_object.country_id).all()
        for goals in goals_list:
            self.goals += goals[0]
            self.num_of_matches_played += 1
        return self.goals / self.num_of_matches_played

    def get_all_group_stage_goals_and_num_of_matches_played(self):
        """
        This goes through every group stage game and gets all the goals that the country scored. It also calculates
        the number of group games that they played
        Returns
        -------
        None
        """
        all_group_games = self.sess.query(Match.match_id).filter(Match.stage_id < 9).all()
        for game in all_group_games:
            goals = self.sess.query(CountryMatch.score).filter_by(match_id=game[0],
                                                                  country_id=self.country_object.country_id).first()
            if goals != None:
                self.group_goals += goals[0]
                self.num_of_group_matches_played += 1

    def get_all_ko_goals_and_num_of_matches_played(self):
        """
        This goes through every knockout game and gets all the goals that the country scored. It also calculates
        the number of group games that they played
        Returns
        -------
        None
        """
        all_ko_games = self.sess.query(Match.match_id).filter(Match.stage_id > 8).all()
        for game in all_ko_games:
            goals = self.sess.query(CountryMatch.score).filter_by(match_id=game[0],
                                                                  country_id=self.country_object.country_id).first()
            if goals != None:
                self.ko_goals += goals[0]
                self.num_of_ko_matches_played += 1

    def get_country_they_lost_or_won_to_most(self):
        """
        this gets all the games that a country won and keeps count of the number of times that they beat or lost
        to a country
        Returns
        -------
        None
        """

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
                self.number_of_wins_dict[country_name[0]] += 1

            if opposition.result == 'win':
                country_name = self.sess.query(Country.country_name).filter_by(country_id=opposition.country_id).first()
                self.number_of_loses_dict[country_name[0]] += 1

    def furthest_got_and_average_place(self, country_name):
        '''
        This gets the furthest place that the country got to in all simulations as well filling in dictionaries about
        how they did in each simulation in order to create figures in the GUI

        Parameters
        ----------
        country_name: name of the country

        Returns
        -------
        self.dict_of_where_they_came: This is a dictionary of how many times the country got knocked out in each stage
        '''
        cn = str(country_name)
        self.percentage_get_to_dict = {'Group': 0, 'Round of 16': 0, 'Quarter-final': 0, 'Semi-final': 0, 'Final': 0,
                                       'Win': 0}
        self.country_object = self.sess.query(Country).filter_by(country_name=cn).first()
        self.dict_of_where_they_came = {'Group': 0, 'Round of 16': 0, 'Quarter-final': 0, 'Semi-final': 0, 'Final': 0,
                                        'Win': 0}
        highest_is_winner = False
        for i in range(1, 101):
            win = False
            highest_in_sim = 0
            all_games_in_sim = self.sess.query(CountryMatch.match_id).filter_by(
                country_id=self.country_object.country_id, simulation_number=i).all()
            for match in all_games_in_sim:
                stage = self.sess.query(Match.stage_id).filter_by(match_id=match[0]).first()
                if stage[0] > self.highest_stage_id:
                    self.highest_stage_id = stage[0]
                if stage[0] > highest_in_sim:
                    highest_in_sim = stage[0]

            if highest_in_sim == 23:
                match = self.sess.query(Match.match_id).filter_by(stage_id=23, simulation_number=i).first()
                game = self.sess.query(CountryMatch).filter_by(match_id=match[0], simulation_number=i).all()

                if game[0].result == 'win' and game[0].country_id == self.country_object.country_id:
                    win = True
                    highest_is_winner = True
                elif game[1].result == 'win' and game[1].country_id == self.country_object.country_id:
                    win = True
                    highest_is_winner = True

            self.append_to_dict_where_came(highest_in_sim, win)
            self.append_to_percentage_get_dict(highest_in_sim, win)

        if highest_is_winner:
            self.highest_stage = 'Winner'

        else:
            self.highest_stage = self.sess.query(Stage.level).filter_by(stage_id=self.highest_stage_id).first()
            self.highest_stage = self.highest_stage[0]

        return self.dict_of_where_they_came



    def append_to_dict_where_came(self, highest_in_sim, win):
        """
        This appends the necessary information into the dictionary
        Parameters
        ----------
        highest_in_sim: This is the stage that they got to in the simulation
        win: This is a boolean value for whether they won the WC

        Returns
        -------
        None
        """
        if win:
            self.dict_of_where_they_came['Win'] += 1
        elif highest_in_sim < 9:
            self.dict_of_where_they_came['Group'] += 1
        elif 8 < highest_in_sim < 17:
            self.dict_of_where_they_came['Round of 16'] += 1
        elif 16 < highest_in_sim < 21:
            self.dict_of_where_they_came['Quarter-final'] += 1
        elif highest_in_sim == 21 or highest_in_sim == 22:
            self.dict_of_where_they_came['Semi-final'] += 1
        elif highest_in_sim == 23:
            self.dict_of_where_they_came['Final'] += 1

    def append_to_percentage_get_dict(self, highest_in_sim, win):
        """
        This appends the necessary information into the dictionary
        Parameters
        ----------
        highest_in_sim: This is the stage that they got to in the simulation
        win: This is a boolean value for whether they won the WC

        Returns
        -------
        None
        """
        if highest_in_sim > 0:
            self.percentage_get_to_dict['Group'] += 1
        if 8 < highest_in_sim:
            self.percentage_get_to_dict['Round of 16'] += 1
        if 16 < highest_in_sim:
            self.percentage_get_to_dict['Quarter-final'] += 1
        if highest_in_sim > 20:
            self.percentage_get_to_dict['Semi-final'] += 1
        if highest_in_sim == 23:
            self.percentage_get_to_dict['Final'] += 1
        if win:
            self.percentage_get_to_dict['Win'] += 1

    def average_goals_conceded(self):
        """
        This gets all the games that the user played. It then uses the id of the other country in the game to find
        the goals that they scored in the match. This is then added to the total and the number of matches is
        incremented by 1

        Returns
        -------
        None
        """

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
        """
        This gets the number of goals conceded in the group stage and knockout and calculates the number of games
        they played in both

        Returns
        -------
        None
        """
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
        """
        This gets the number of times that the country won the WC
        Returns
        -------
        None
        """
        for i in range(1, 101):
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
        """
        This goes through very game that the country played and works out how many times they played each country

        Returns
        -------
        None
        """
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
        """
        This goes through very game that the country played and works out how many times they beat and lost to each country

        Returns
        -------
        None
        """
        list_of_countries = ['Argentina', 'France', 'England', 'Belgium', 'Brazil',
                             'Netherlands', 'Portugal', 'Spain',
                             'Italy', 'Croatia', 'Uruguay', 'Morocco', 'USA', 'Columbia',
                             'Mexico', 'Germany', 'Senegal', 'Japan',
                             'Switzerland', 'Iran', 'Denmark', 'Korea', 'Australia',
                             'Ukraine', 'Austria', 'Sweden', 'Hungary', 'Nigeria',
                             'Wales', 'Poland', 'Equador', 'Serbia']
        percentage_list_won = []
        percentage_list_lost = []
        for country in list_of_countries:
            number_won = self.number_of_wins_dict[country]
            number_lost = self.number_of_loses_dict[country]
            number_played = self.number_of_times_played_dict[country]
            try:
                percentage_won = number_won / number_played
            except:
                percentage_won = 0
            try:
                percentage_lost = number_lost / number_played
            except:
                percentage_lost = 0
            percentage_list_won.append(percentage_won)
            percentage_list_lost.append(percentage_lost)

        self.team_they_beat_the_highest_percentage_of_times = list_of_countries[
            percentage_list_won.index(max(percentage_list_won))]
        self.team_they_lost_to_the_highest_percentage_of_times = list_of_countries[
            percentage_list_lost.index(max(percentage_list_lost))]


if __name__ == '__main__':
    g = Analyse()
    g.controller('England')
