from create_group_matches import GroupGenerator, CreateMatches
from run_group_matches import MakeMatches
from redo_find_group_results import FindGroupResults
from knockouts import Knockouts

for i in range(1,20):
    gg = GroupGenerator()
    print(gg.collate_groups())
    cm = CreateMatches()
    print(cm.creates_ids(i))

    mm = MakeMatches()
    print(mm.sim_the_game(i))

    fgr = FindGroupResults()
    print(fgr.collective())

    ko = Knockouts()
    print(ko.collate(i))

