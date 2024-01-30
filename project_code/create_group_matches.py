from random import randint, sample
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import update
from project_code.sim_game import SimGame
from project_code.models import Country, CountryMatch


class GroupGenerator:
    def __init__(self):
        self.engine = create_engine('sqlite:///World_cup.sqlite3', echo=True)
        self.collated_groups = []
        self.sess = Session(self.engine)
        self.team = ''

        self.countries = [sample(self.sess.query(Country).filter_by(tier=i + 1).all(),
                                 k=len(self.sess.query(Country).filter_by(tier=i + 1).all())) for i in range(4)]

    def group_draw(self):
        # Creates a single group by taking a random country from each tier and adding it to a list
        group = []
        for i, tier in enumerate(self.countries):
            self.team = tier[randint(0, len(tier) - 1)]
            group.append(self.team)
            tier.remove(self.team)
        return group

    def collate_groups(self):
        # Iterates through group_draw and creates all 8 groups and then adds it to collated groups to make one big
        # list of lists.
        collated_groups = []
        for i in range(8):
            collated_groups.append(self.group_draw())

        self.collated_groups = collated_groups

        return self.collated_groups


class CreateMatches:
    # Fills in intial information so that it lays out which matches play in what order and makes it easy to simulate
    # through all games
    def __init__(self):

        self.match_id = None
        self.match_id_counter = -1
        self.group_generator = GroupGenerator()
        self.list_of_groups = []
        self.list_of_groups = self.group_generator.collate_groups()
        self.object_list = []
        self.engine = create_engine('sqlite:///World_cup.sqlite3', echo=True)
        self.sess = Session(self.engine)
        self.order = [[0], [2], [1], [3], [2], [1], [0], [3], [0], [1], [2], [3]]
        self.list = []

    def get_match_id(self,sim_num):
        self.match_id = self.sess.query(CountryMatch.match_id).filter_by(simulation_number=sim_num).order_by(CountryMatch.match_id.desc()).first()
        if self.match_id is None:
            self.match_id =0

    def creates_ids(self, sim_num):
        # creates the ID for each entry and sends it to create_initial_country_match to commit
        self.get_match_id(sim_num)
        for group in self.list_of_groups:
            for i in range(len(self.order)):
                self.update_every_second_time()
                country_object = group[self.order[i][0]]
                country_object_id = country_object.country_id
                self.object_list.append(country_object)
                self.create_initial_country_match(country_object_id, sim_num)
        self.sess.commit()

    def create_initial_country_match(self, id, sim_num):
        '''Can make list and commit them all at one'''
        # Commits the id
        add_to_country_match = CountryMatch(country_id=id, match_id=self.match_id, simulation_number=sim_num)
        self.sess.add(add_to_country_match)


    def update_every_second_time(self):
        self.match_id_counter += 1
        if self.match_id_counter % 2 == 0:
            self.match_id += 1
        return self.match_id


if __name__ == '__main__':
    ff = GroupGenerator()
    print(ff.collate_groups())
    gg = CreateMatches()
    print(gg.creates_ids(1))
