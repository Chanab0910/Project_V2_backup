from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from models_2 import Country, Group

engine = create_engine('sqlite:///World_cup_2.sqlite3', echo=True)

sess = Session(engine)

def sim_game_object(self, home_country, away_country):
    self.home_country_attack = self.get_attack(home_country)
    self.away_country_attack = self.get_attack(away_country)
    self.home_country_defense = self.get_defense(home_country)
    self.away_country_defense = self.get_defense(home_country)
    self.Home_team_score = self.calculate_goals(self.home_country_attack[0], self.home_country_defense[0])
    self.Away_team_score = self.calculate_goals(self.away_country_attack[0], self.home_country_defense[0])
    if self.Home_team_score > self.Away_team_score:
        self.add_to_match(home_country)
        pass
    elif self.Home_team_score < self.Away_team_score:
        self.add_to_match(away_country)
        pass
    else:
        self.add_to_match('draw')
        pass
    self.add_to_country_match(home_country, away_country)
    self.add_to_group_match()
    # self.add_to_group()

countries = sess.query(Country).all()
groups = sess.query(Group).all()

australia = countries[0]
austria = countries[0]
belgium = countries[0]
canada = countries[0]
# PUts australia in the first group
australia.group = groups[0]
austria.group = groups[0]
belgium.group= groups[0]
canada = groups[0]

print(groups[0].countries)


# Simulate a match
# result = sim_match(australia, belgium)

sess.commit()
sess.close()


