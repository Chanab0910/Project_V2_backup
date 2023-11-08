from sqlalchemy import create_engine
from models_2 import Base

engine = create_engine('sqlite:///World_cup_2.sqlite3', echo=True)
Base.metadata.create_all(engine)
