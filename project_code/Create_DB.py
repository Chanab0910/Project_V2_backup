from sqlalchemy import create_engine
from models import Base

engine = create_engine('sqlite:///World_cup.sqlite3', echo=True)
Base.metadata.create_all(engine)

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from project_code.models import Country, Stage

engine = create_engine('sqlite:///World_cup.sqlite3', echo=True)
sess = Session(engine)

countries = [Country(country_name="Argentina", attack=93, defense=90, tier=1),
             Country(country_name="France", attack=89, defense=88, tier=1),
             Country(country_name="England", attack=92, defense=87, tier=1),
             Country(country_name="Belgium", attack=88, defense=85, tier=1),
             Country(country_name="Brazil", attack=90, defense=87, tier=1),
             Country(country_name="Netherlands", attack=86, defense=85, tier=1),
             Country(country_name="Portugal", attack=85, defense=84, tier=1),
             Country(country_name="Spain", attack=86, defense=84, tier=1),
             Country(country_name="Italy", attack=85, defense=89, tier=2),
             Country(country_name="Croatia", attack=80, defense=80, tier=2),
             Country(country_name="Uruguay", attack=81, defense=80, tier=2),
             Country(country_name="Morocco", attack=77, defense=78, tier=2),
             Country(country_name="USA", attack=74, defense=74, tier=2),
             Country(country_name="Columbia", attack=73, defense=72, tier=2),
             Country(country_name="Mexico", attack=72, defense=72, tier=2),
             Country(country_name="Germany", attack=81, defense=82, tier=2),
             Country(country_name="Senegal", attack=78, defense=79, tier=3),
             Country(country_name="Japan", attack=75, defense=76, tier=3),
             Country(country_name="Switzerland", attack=73, defense=74, tier=3),
             Country(country_name="Iran", attack=70, defense=71, tier=3),
             Country(country_name="Denmark", attack=74, defense=71, tier=3),
             Country(country_name="Korea", attack=76, defense=72, tier=3),
             Country(country_name="Australia", attack=70, defense=70, tier=3),
             Country(country_name="Ukraine", attack=74, defense=72, tier=3),
             Country(country_name="Austria", attack=69, defense=67, tier=4),
             Country(country_name="Sweden", attack=71, defense=69, tier=4),
             Country(country_name="Hungary", attack=70, defense=68, tier=4),
             Country(country_name="Nigeria", attack=67, defense=67, tier=4),
             Country(country_name="Wales", attack=71, defense=70, tier=4),
             Country(country_name="Poland", attack=67, defense=65, tier=4),
             Country(country_name="Equador", attack=68, defense=66, tier=4),
             Country(country_name="Serbia", attack=67, defense=66, tier=4),
             ]

stages = [
    Stage(stage_id=1, level='Group', sequence='1'),
    Stage(stage_id=2, level='Group', sequence='2'),
    Stage(stage_id=3, level='Group', sequence='3'),
    Stage(stage_id=4, level='Group', sequence='4'),
    Stage(stage_id=5, level='Group', sequence='5'),
    Stage(stage_id=6, level='Group', sequence='6'),
    Stage(stage_id=7, level='Group', sequence='7'),
    Stage(stage_id=8, level='Group', sequence='8'),
    Stage(stage_id=9, level='Round of 16', sequence='1'),
    Stage(stage_id=10, level='Round of 16', sequence='2'),
    Stage(stage_id=11, level='Round of 16', sequence='3'),
    Stage(stage_id=12, level='Round of 16', sequence='4'),
    Stage(stage_id=13, level='Round of 16', sequence='5'),
    Stage(stage_id=14, level='Round of 16', sequence='6'),
    Stage(stage_id=15, level='Round of 16', sequence='7'),
    Stage(stage_id=16, level='Round of 16', sequence='8'),
    Stage(stage_id=17, level='Quarter-finals', sequence='1'),
    Stage(stage_id=18, level='Quarter-finals', sequence='2'),
    Stage(stage_id=19, level='Quarter-finals', sequence='3'),
    Stage(stage_id=20, level='Quarter-finals', sequence='4'),
    Stage(stage_id=21, level='Semi-finals', sequence='1'),
    Stage(stage_id=22, level='Semi-finals', sequence='2'),
    Stage(stage_id=23, level='Final', sequence='1'),
    Stage(stage_id=24, level='R1', sequence='1'),
]

sess.add_all(stages)
sess.add_all(countries)
sess.commit()
sess.close()