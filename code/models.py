from sqlalchemy import Column, Integer, String, Table, UniqueConstraint, ForeignKey, BLOB
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()


class Country(Base):
    __tablename__ = 'Country'
    id = Column('id', Integer, primary_key=True)
    country_name = Column('country_name', String, unique=True, nullable=False)
    attack = Column('attack', Integer, unique=False, nullable=False)
    defense = Column('defense', Integer, unique=False, nullable=False)
    tier = Column('tier', Integer, unique=False, nullable=False)

    def __repr__(self):
        return f'Country({self.country_name})'


class Match(Base):
    __tablename__ = 'Match'
    id = Column('id', Integer, primary_key=True)
    Home_team = Column(String, primary_key=True, unique=False, nullable=False)
    Away_team = Column(String, primary_key=True, unique=False, nullable=False)
    Stage = Column(Integer, unique=False, nullable=False)
    Home_goals = Column(Integer, unique=False, nullable=False)
    Away_goals = Column(Integer, unique=False, nullable=False)
    Winner = Column(String, unique=False, nullable=False)

    def __repr__(self):
        return f'Match({self.Home_team}) v Match({self.Away_team})'
