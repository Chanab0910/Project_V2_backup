from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from project_code.models import Country, Stage

engine = create_engine('sqlite:///World_cup.sqlite3', echo=True)
sess = Session(engine)

stages = [
    Stage(stage_id=1, level='Group', sequence='A'),
    Stage(stage_id=2, level='Group', sequence='B'),
    Stage(stage_id=3, level='Group', sequence='C'),
    Stage(stage_id=4, level='Group', sequence='D'),
    Stage(stage_id=5, level='Group', sequence='E'),
    Stage(stage_id=6, level='Group', sequence='F'),
    Stage(stage_id=7, level='Group', sequence='G'),
    Stage(stage_id=8, level='Group', sequence='H'),
    Stage(stage_id=9, level='R16', sequence='1'),
    Stage(stage_id=10, level='R16', sequence='2'),
    Stage(stage_id=11, level='R16', sequence='3'),
    Stage(stage_id=12, level='R16', sequence='4'),
    Stage(stage_id=13, level='R16', sequence='5'),
    Stage(stage_id=14, level='R16', sequence='6'),
    Stage(stage_id=15, level='R16', sequence='7'),
    Stage(stage_id=16, level='R16', sequence='8'),
    Stage(stage_id=17, level='R8', sequence='1'),
    Stage(stage_id=18, level='R8', sequence='2'),
    Stage(stage_id=19, level='R8', sequence='3'),
    Stage(stage_id=20, level='R8', sequence='4'),
    Stage(stage_id=21, level='R4', sequence='1'),
    Stage(stage_id=22, level='R4', sequence='2'),
    Stage(stage_id=23, level='R2', sequence='1'),
    Stage(stage_id=24, level='R1', sequence='1'),
]

sess.add_all(stages)
sess.commit()
sess.close()
