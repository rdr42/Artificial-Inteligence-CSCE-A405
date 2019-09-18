class Node:
  def __init__(self,board,neighbors,child):
    self.parent = None
    self.board = board
    self.edge = neighbors
    self.child = child
    self.cost = 0
    self.misplacedTiles = None
    self.h = 0
    self.g = 0
    self.f = 0
