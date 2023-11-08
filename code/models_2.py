from sqlalchemy import Column, Integer, String, Table, UniqueConstraint, ForeignKey, BLOB
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
    group_id = Column(Integer, ForeignKey("group.group_id"), unique=False)
    group = relationship("Group", back_populates="countries")

    def __repr__(self):
        return f'Country({self.country_name})'


class Group(Base):
    __tablename__ = 'group'
    group_id = Column(Integer, primary_key=True, autoincrement=True)
    # match_id = Column(Integer, primary_key=True)
    countries = relationship("Country", back_populates="group")

    def __repr__(self):
        return f'{self.Group_id, self.Match_id}'

