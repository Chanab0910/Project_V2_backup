from random import randint, shuffle, sample, random

from numpy import random
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from code.models import Country, Match, Group_match, Country_match, Group_points


class FindGroupResults:
    def __init__(self):
        self.winner = None
        self.engine = create_engine('sqlite:///World_cup.sqlite3', echo=True)
        self.sess = Session(self.engine)

    def get_match_winner(self):
        self.winner = self.sess.query(Match.Winner).filter_by(Match.Match_id == Group_match.Match_id)
        return self.winner

    def

