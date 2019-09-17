from Method import *
#n is some state
class Heuristic:
  def __init__(self,n,start,goal):
    self.n = n
    self.start = start
    self.goal = goal

#Given the heuristic n, return proper method.
  def hMethod(self):
    m = Method(self.start,self.goal)
    if self.n == 0:
      return m.bfs()
    elif self.n == 1:
      return m.aMisplaced()
    elif self.n == 2:
      return m.aManhattan()
    elif self.n == 3:
      return m.aGaschnig()
    else:
      return 'error'
