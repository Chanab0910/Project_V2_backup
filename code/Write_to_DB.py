from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from code.models import Country, Match

engine = create_engine('sqlite:///World_cup_1.sqlite3', echo=True)
sess = Session(engine)


countries = [Country(country_name="Argentina", attack=84, defense=82, tier=1),
             Country(country_name="Australia", attack=70, defense=70, tier=2),
             Country(country_name="Austria", attack=78, defense=77, tier=3),
             Country(country_name="Belgium", attack=81, defense=78, tier=4),
             Country(country_name="Canada", attack=77, defense=70, tier=1),
             Country(country_name="Croatia", attack=77, defense=78, tier=2),
             Country(country_name="Czech Republic", attack=77, defense=75, tier=3),
             Country(country_name="Denmark", attack=75, defense=79, tier=4),
             Country(country_name="England", attack=85, defense=82, tier=1),
             Country(country_name="Finland", attack=72, defense=68, tier=2),
             Country(country_name="France", attack=85, defense=83, tier=3),
             Country(country_name="Germany", attack=80, defense=80, tier=4),
             Country(country_name="Hungary", attack=76, defense=73, tier=1),
             Country(country_name="Iceland", attack=70, defense=71, tier=2),
             Country(country_name="Ireland", attack=70, defense=71, tier=3),
             Country(country_name="Italy", attack=81, defense=81, tier=4),
             Country(country_name="Mexico", attack=78, defense=76, tier=1),
             Country(country_name="Ghana", attack=81, defense=74, tier=2),
             Country(country_name="Netherlands", attack=83, defense=82, tier=3),
             Country(country_name="Morocco", attack=77, defense=78, tier=4),
             Country(country_name="Norway", attack=82, defense=74, tier=1),
             Country(country_name="Poland", attack=79, defense=75, tier=2),
             Country(country_name="Portugal", attack=84, defense=83, tier=3),
             Country(country_name="Romania", attack=70, defense=69, tier=4),
             Country(country_name="Scotland", attack=72, defense=76, tier=1),
             Country(country_name="Spain", attack=83, defense=83, tier=2),
             Country(country_name="Sweden", attack=78, defense=75, tier=3),
             Country(country_name="Ukraine", attack=74, defense=72, tier=4),
             Country(country_name="USA", attack=74, defense=74, tier=1),
             Country(country_name="Wales", attack=74, defense=73, tier=2),
             Country(country_name="Japan", attack=75, defense=76, tier=3),
             Country(country_name="China", attack=78, defense=73, tier=4),
             ]

sess.add_all(countries)
sess.commit()
sess.close()