class Node:
  def __init__(self,board,neighbors,parent,child):
    self.parent = parent
    self.board = board
    self.edge = neighbors
    self.child = child
    self.counter = 0
    self.misplacedTiles = None


