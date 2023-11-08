from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from code.models_2 import Country, Group

engine = create_engine('sqlite:///World_cup_2.sqlite3', echo=True)
sess = Session(engine)

countries = [Country(country_name="Australia", attack=70, defense=70, tier=2),
             Country(country_name="Austria", attack=78, defense=77, tier=3),
             Country(country_name="Belgium", attack=81, defense=78, tier=4),
             Country(country_name="Canada", attack=77, defense=70, tier=1),
             ]

# def add_country(id, name, attack, defense, tier):
#     country = Country(id=id, ountry_name='attack', attack=attack, defense=defense, tier=tier)
#     return sess.add(country)
groups = [Group(),
          Group(),
          ]

sess.add_all(countries)
sess.add_all(groups)
sess.commit()
sess.close()
