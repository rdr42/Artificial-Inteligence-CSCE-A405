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
      return m.BFS()
    if self.n == 1:
      return m.MISP()
    if self.n == 2:
      return m.MAN()
    else:
      return 'error'
