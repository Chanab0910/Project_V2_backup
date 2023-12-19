from create_group_matches import GroupGenerator, CreateMatches
from run_group_matches import MakeMatches
from find_group_results import FindGroupResults
from knockouts import Knockouts

gg = GroupGenerator()
print(gg.collate_groups())
cm = CreateMatches()
print(cm.creates_ids())

mm = MakeMatches()
print(mm.sim_the_game())

fgr = FindGroupResults()
print(fgr.collective())

ko = Knockouts()
print(ko.collate())

