from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from code.models import Country, CountryMatch


def update_table(self, match_id, home_team_id, away_team_id, home_team_score, away_team_score):
    match_pair = sess.query(CountryMatch).filter(match_id=match_id).all()



engine = create_engine('sqlite:///World_cup.sqlite3', echo=True)
sess = Session(engine)





sess.close()