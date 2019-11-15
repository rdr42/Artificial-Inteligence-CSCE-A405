class Node:
  def __init__(self,node):
    self.node = node
    self.matrix = None

  def sanitize(self):
    matrix = []
    temp = []
    for i in self.node:
      for j in i:
        if j != ',':
          temp.append(int(j))
      matrix.append(temp)
      temp = []
    self.matrix = matrix
  
  def printBoard(self):
    print(' -------------------------')
    print(self.matrix[0])
    print(self.matrix[1])
    print(self.matrix[2])
    print(self.matrix[3])
    print(self.matrix[4])
    print(self.matrix[5])
    print(' -------------------------')

class Board:
  def __init__(self):
    self.board = []