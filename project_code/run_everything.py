from create_group_matches import GroupGenerator, CreateMatches
from run_group_matches import RunMatches
from redo_find_group_results import FindGroupResults
from knockouts import Knockouts

for i in range(1,10):
    gg = GroupGenerator()
    gg.collate_groups()
    cm = CreateMatches()
    cm.creates_ids(i)

    mm = RunMatches()
    mm.sim_the_game(i)

    fgr = FindGroupResults()
    fgr.collective(i)

    ko = Knockouts()
    ko.collate(i)

