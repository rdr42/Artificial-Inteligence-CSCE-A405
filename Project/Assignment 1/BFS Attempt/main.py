class Node:
  def __init__(self,board = None):
    self.parent = None
    self.board = board
    self.edge = []
    self.child = False
    self.counter = 0
  


class Graph:
  def __init__(self):
    self.nodes = []
    self.graph = None
    
  def addNewNode(self,node):
    self.nodes.append(node)

class Board:
  def getNeighbors(self,element,board):
    index = board.index(element)
    if index == 0:
      return [self.getPiece(1,board),self.getPiece(3,board)]
    elif index == 1:
      return [self.getPiece(0,board),self.getPiece(2,board),self.getPiece(4,board)]
    elif index == 2:
      return [self.getPiece(1,board),self.getPiece(5,board)]
    elif index == 3:
      return [self.getPiece(0,board),self.getPiece(4,board),self.getPiece(6,board)]
    elif index == 4:
      return [self.getPiece(1,board),self.getPiece(3,board),self.getPiece(5,board), self.getPiece(7,board)]
    elif index == 5:
      return [self.getPiece(2,board),self.getPiece(4,board),self.getPiece(8,board)]
    elif index == 6:
      return [self.getPiece(3,board),self.getPiece(7,board)]
    elif index == 7:
      return [self.getPiece(6,board),self.getPiece(4,board),self.getPiece(8,board)]
    elif index == 8:
      return [self.getPiece(5,board),self.getPiece(7,board)]

  def getPiece(self,element,board):
    return board[element]

  def switchPieces(self,pieceA,pieceB,board):
    boardCopy = board.copy()
    indexA = board.index(pieceA)
    indexB = board.index(pieceB)
    boardCopy[indexA] = pieceB
    boardCopy[indexB] = pieceA
    return boardCopy
  
  def printBoard(self,board):
    el = board
    print(" ------------- ")
    print("||",el[0],"|",el[1],"|",el[2],"||")
    print("")
    print("||",el[3],"|",el[4],"|",el[5],"||")
    print("")
    print("||",el[6],"|",el[7],"|",el[8],"||")
    print(" ------------- ")

a = Board()
start = [1,2,3,0,4,5,6,7,8]
end = [1,2,3,8,0,4,7,6,5]

queue = []
discovered = []
explored = []

edges = a.getNeighbors(0,start)
n = Node(board=start)
n.edge = edges
g = Graph()
n.counter = 0
root = n
g.addNewNode(n)
queue.append(n)

nodes_ = []
counter = 1
done = False
found = None
while len(queue) > 0 and not done:
  v = queue.pop()
  if(v.board not in discovered):
    discovered.append(v.board)
  if v.board == end:
    found = v
    break
  for i in g.nodes:
    for j in i.edge:
      bnew = a.switchPieces(0,j,i.board)
      if bnew == end:
        newNode = Node(bnew)
        newNode.edge = a.getNeighbors(0,bnew)
        discovered.append(newNode.board)
        newNode.parent = i
        newNode.child = True
        nodes_.append(newNode)
        g.addNewNode(newNode)
        found = newNode
        done = True
        break
      else:
        if bnew not in discovered and bnew != start:
          newNode = Node(bnew)
          newNode.edge = a.getNeighbors(0,bnew)
          discovered.append(newNode.board)
          newNode.parent = i
          newNode.child = True
          queue.append(newNode)
          nodes_.append(newNode)
          counter = counter + 1
      if done:
        break
    if done:
      break
  for i in queue:
    g.addNewNode(i)

parent = []
done = False
counter = 0
while not done:
  a.printBoard(found.board)
  if found.parent == None:
    print(counter,' Moves!')
    break
  found = found.parent
  counter = counter + 1
