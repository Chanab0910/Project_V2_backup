import pytest
from create_groups import GroupGenerator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Country, Match
import models as m
import random

# Connect to the activities database
engine = create_engine('sqlite:///:memory:', echo=True)


@pytest.fixture
def session():
    Session = sessionmaker(bind=engine)
    db_session = Session()
    yield db_session
    db_session.rollback()
    db_session.close()


@pytest.fixture(autouse=True)
def setup_db(session, request):
    def teardown():
        m.Base.metadata.drop_all(engine)

    m.Base.metadata.create_all(engine)

    # Create some content within the test database
    countries = [Country(country_name='England', attack=78, defense=85, tier=1),
                 # Country('Spain', 87, 83, 2),
                 # Country('Germany', 81, 79, 3),
                 # Country('Sweden', 78, 76, 4)
                 ]

    # Add changes to the database and commit
    session.add_all(countries)
    session.commit()

    request.addfinalizer(teardown)


def test_Countries(session):
    countries = session.query(m.Country).all()
    assert len(countries) == 4



def test_group_draw():
    assert True
