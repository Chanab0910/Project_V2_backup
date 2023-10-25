from sqlalchemy import Column, Integer, String, Table, UniqueConstraint, ForeignKey, BLOB
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()


class Country(Base):
    __tablename__ = 'Country'
    country_id = Column('id', Integer, primary_key=True, autoincrement=True)
    country_name = Column('country_name', String, unique=True, nullable=False)
    attack = Column('attack', Integer, unique=False, nullable=False)
    defense = Column('defense', Integer, unique=False, nullable=False)
    tier = Column('tier', Integer, unique=False, nullable=False)

    def __repr__(self):
        return f'Country({self.country_name})'


class Match(Base):
    __tablename__ = 'Match'
    Match_id = Column('id', Integer, primary_key=True, autoincrement=True)
    Stage = Column(Integer, unique=False, nullable=False)
    Home_goals = Column(Integer, unique=False, nullable=False)
    Away_goals = Column(Integer, unique=False, nullable=False)
    Winner = Column(String, unique=False, nullable=False)

    def __repr__(self):
        return f'Match({self.Home_team}) v Match({self.Away_team})'


class Country_match(Base):
    __tablename__ = 'Country_match'
    Match_id = Column('id', Integer, primary_key=True)
    Home_team_id = Column(String, primary_key=True, unique=False, nullable=False)
    Away_team_id = Column(String, primary_key=True, unique=False, nullable=False)

    def __repr__(self):
        return f'Match({self.Home_team}) v Match({self.Away_team})'


class Group_match(Base):
    __tablename__ = 'Group_match'
    Group_id = Column(Integer, primary_key=True)
    Match_id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f'{self.Group_id, self.Match_id}'


class Group_points(Base):
    __tablename__ = 'Group_points'
    Group_id = Column(Integer, primary_key=True,autoincrement=True)
    team1_points = Column(Integer)
    team2_points = Column(Integer)
    team3_points = Column(Integer)
    team4_points = Column(Integer)

    def __repr__(self):
        return f'{self.Group_id}'
