from project_code.analyse_results import Analyse
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from general_analysis import GeneralAnalysis
engine = create_engine('sqlite:///World_cup.sqlite3', echo=True)

sess = Session(engine)

ga = GeneralAnalysis()
a = ga.get_stats()
print(a)