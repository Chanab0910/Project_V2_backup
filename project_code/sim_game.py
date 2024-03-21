from numpy import random
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from project_code.models import Match


class SimGame:
    def __init__(self):
        self.result = ()
        self.group_input = None
        self.group_id = 0
        self.country_match_input = None

        self.goals = None
        self.time = 90

        self.base = 0.0128125
        self.engine = create_engine('sqlite:///World_cup.sqlite3', echo=False)
        self.order = [[0, 2], [1, 3], [2, 1], [0, 3], [0, 1], [2, 3]]
        self.sess = Session(self.engine)
        self.team = ''

    def sim_game_object(self, home_country, away_country, stage, match_number,sim_num,match_id):
        """
        takes the object of each country, gets its attack and defense and runs each team through calculate goals.It then determines who won
        Parameters
        ----------
        home_country: the home country
        away_country: the away country
        stage: The stage that the match is in
        match_number: The number of the match in the stage
        sim_num: The simulation number thst the game is taking place in
        match_id: The match_id

        Returns
        -------
        self.result: this is the result of the match
        """

        home_country_attack = home_country.attack
        away_country_attack = away_country.attack
        home_country_defense = home_country.defense
        away_country_defense = away_country.defense
        Home_team_score = self.calculate_goals(home_country_attack, away_country_defense)
        Away_team_score = self.calculate_goals(away_country_attack, home_country_defense)
        self.add_to_match(stage, match_number,sim_num,match_id)

        if Home_team_score > Away_team_score:
            return 'win', Home_team_score, Away_team_score

        elif Home_team_score < Away_team_score:

            return 'loss', Home_team_score, Away_team_score

        else:
            if stage < 9:
                return 'draw', Home_team_score, Away_team_score
            else:
                self.extra_time(Home_team_score,Away_team_score,home_country, away_country, stage, match_number)
                return self.result

    def calculate_goals(self, attack, defense):
        """
        This calculates the number of goals that a country scores in a match
        Parameters
        ----------
        attack: The attack of the country
        defense: The defense of the opponent

        Returns
        -------
        self.goals: number of goals that the country scored
        """
        self.goals =0
        for i in range(self.time):
            self.variablility = random.uniform(0,0.005)
            self.goals += random.poisson(self.base * (attack / defense) + self.variablility)
        return self.goals

    def add_to_match(self, stage, match_number,sim_num,match_id):
        """
        Adds the match to the match table
        Parameters
        ----------
        stage:The stage that the match is in
        match_number: The number of the match in the stage
        sim_num: The simulation number thst the game is taking place in
        match_id: The match_id

        Returns
        -------
        None
        """
        match_addition = Match(stage_id=stage, match_number=match_number,simulation_number=sim_num,match_id =match_id)
        self.sess.add(match_addition)
        self.sess.commit()

    def extra_time(self, home_goals, away_goals,home_country, away_country):
        """
        This simulates extra time
        Parameters
        ----------
        home_goals: The number of goals that the home country is on
        away_goals: The number of goals that the home country is on
        home_country: the home country
        away_country: the away country

        Returns
        -------
        None
        """
        self.time = 30
        home_country_attack = home_country.attack
        away_country_attack = away_country.attack
        home_country_defense = home_country.defense
        away_country_defense = away_country.defense
        Home_team_score = self.calculate_goals(home_country_attack, away_country_defense) + home_goals
        Away_team_score = self.calculate_goals(away_country_attack, home_country_defense) + away_goals
        self.time = 90
        if Home_team_score > Away_team_score:
            self.result = ('win', Home_team_score, Away_team_score)

        elif Home_team_score < Away_team_score:
            self.result = ('loss', Home_team_score, Away_team_score)

        else:
            self.penalties(Home_team_score, Away_team_score, home_country, away_country)

    def penalties(self,home_goals, away_goals, home_country, away_country,):
        """
        Simulates penalties
        Parameters
        ----------
        home_goals: The number of goals that the home country is on
        away_goals: The number of goals that the home country is on
        home_country: the home country
        away_country: the away country

        Returns
        -------

        """
        stop = False
        home_country_attack = home_country.attack
        away_country_attack = away_country.attack
        home_country_defense = home_country.defense
        away_country_defense = away_country.defense
        self.time = 1
        while not stop:
            Home_team_score = self.calculate_goals(home_country_attack,away_country_defense) + home_goals
            Away_team_score = self.calculate_goals(away_country_attack,home_country_defense) + away_goals
            if Home_team_score > Away_team_score:
                self.result = ('win', Home_team_score, Away_team_score)
                stop = True

            elif Home_team_score < Away_team_score:
                self.result = ('loss', Home_team_score, Away_team_score)
                stop = True


if __name__ == '__main__':
    sm = SimGame()
    print(sm.calculate_goals(78,82))