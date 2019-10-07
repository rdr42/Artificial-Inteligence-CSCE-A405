class Node:
  def __init__(self):
    self.name= None
    self.value = 0
    self.edges = []
    self.isMin = False
    self.isMax = False
    self.alpha = 0
    self.beta = 0
    self.isLeaf = False