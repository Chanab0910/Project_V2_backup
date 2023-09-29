import read_from_db
from random import randint, shuffle, sample
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


class GroupGenerator:
    def __init__(self):
        self.team = ''
        self.groups = [[] for i in range(8)]
        self.countries_in_tiers = []
        self.countries_in_tiers.append(sample(read_from_db.tier1_countries, len(read_from_db.tier1_countries)))
        self.countries_in_tiers.append(sample(read_from_db.tier2_countries, len(read_from_db.tier2_countries)))
        self.countries_in_tiers.append(sample(read_from_db.tier3_countries, len(read_from_db.tier3_countries)))
        self.countries_in_tiers.append(sample(read_from_db.tier4_countries, len(read_from_db.tier4_countries)))

    def group_draw(self):
        group = []
        for i, group in enumerate(self.groups):
            self.team = self.countries_in_tiers[i][randint(0, len(self.countries_in_tiers[i]))]
            group.append(self.team)
            self.countries_in_tiers[i].remove(self.team)
        return group


class SimulateGroups:
    def __init__(self):
        self.Home_team_score = None
        self.base = 0.0128125
        self.groups = GroupGenerator.group_draw()
        self.engine = self.create_engine('sqlite:///World_cup.sqlite3', echo=True)

        self.sess = self.Session(self.engine)

    def sim_match(self):
        for group in self.groups:
            if self.calculate_goals(
                    self.sess.query(self.Country.Attack).filter_by(self.Country.Country_name == group[0])):
                ...

    def calculate_goals(self):
        ...
