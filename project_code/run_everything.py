from create_group_matches import GroupGenerator, CreateMatches
from run_group_matches import MakeMatches
from find_group_results import FindGroupResults
from knockouts import Knockouts

group_generator = GroupGenerator()
group_generator.collate_groups()

create_matches = CreateMatches()
create_matches.creates_ids()

make_matches = MakeMatches()
make_matches.sim_the_game()

find_group_results_ = FindGroupResults()
find_group_results_.collective()

knockouts_ = Knockouts()
knockouts_.collate()