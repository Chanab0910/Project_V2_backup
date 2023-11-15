from sqlalchemy import Column, Integer, String, Table, UniqueConstraint, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()


class Country(Base):
    __tablename__ = 'country'
    country_id = Column('id', Integer, primary_key=True, autoincrement=True)
    country_name = Column('country_name', String, unique=True, nullable=False)
    attack = Column('attack', Integer, unique=False, nullable=False)
    defense = Column('defense', Integer, unique=False, nullable=False)
    tier = Column('tier', Integer, unique=False, nullable=False)

    def __repr__(self):
        return f'Country({self.country_name})'


class CountryMatch(Base):
    __tablename__ = 'country_match'
    country_match_id = Column('id', Integer, primary_key=True, autoincrement=True)
    match_id = Column('match_id', Integer,)
    country_id = Column('country_id', Integer,)
    score = Column('score', Integer)
    result = Column('result', String)

    def __repr__(self):
        return f'the country_id is {self.country_id}'



class Match(Base):
    __tablename__ = 'match'
    match_id = Column('match_id', Integer, primary_key=True, autoincrement=True)
    stage_id = Column('stage_id', Integer,)
    match_number = Column('match_number', Integer)

    def __repr__(self):
        return f'Match_id: {self.match_id}'


class Stage(Base):
    __tablename__ = 'stage'
    stage_id = Column('stage_id', Integer, primary_key=True)
    sequence = Column('sequence', String)
    level = Column('level', String)
