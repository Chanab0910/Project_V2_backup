from project_code.analyse_results import Analyse
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
engine = create_engine('sqlite:///World_cup.sqlite3', echo=True)
sess = Session(engine)
analyse = Analyse()

a = analyse.controller('England')
