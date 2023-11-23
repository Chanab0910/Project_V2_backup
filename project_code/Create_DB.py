from sqlalchemy import create_engine
from models import Base

engine = create_engine('sqlite:///World_cup.sqlite3', echo=True)
Base.metadata.create_all(engine)