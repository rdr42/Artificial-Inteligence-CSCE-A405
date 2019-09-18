from Heuristic import *
from Board import *

# 0 is BFS
# 1 is Misplaced
# 2 is Manhattam

h = Heuristic(2,[2,3,1,7,0,8,6,5,4],[1,2,3,8,0,4,7,6,5])

h.hMethod()
