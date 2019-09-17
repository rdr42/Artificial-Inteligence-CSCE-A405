from Node import *
from Graph import *
from Board import *

class Method: 
  def __init__(self,start,goal):
    self.start = start
    self.goal = goal
    
  def bfs(self):
    b = Board()
    start = self.start
    end = self.goal
    counter = 0

    queue = []
    discovered = []

    n = Node(start,b.getNeighbors(0,start),None,False)
    n.counter = counter
    g = Graph()
    g.addNewNode(n)
    queue.append(n)


    done = False
    found = None

    while len(queue) > 0 and not done:
      v = queue.pop()
      if v.board not in discovered:
        discovered.append(v.board)

      if v.board == end:
        found = v
        break
      counter += 1
      for i in g.nodes:
        for j in i.edge:
          newBoard = b.switchPieces(0,j,i.board)
          if newBoard == end:
            newNode = Node(newBoard,b.getNeighbors(0,newBoard),i,True)
            newNode.counter = counter
            discovered.append(newNode.board)
            queue.append(newNode)
            found = newNode
            done = True
            break
          else:
            if newBoard not in discovered and newBoard != start:
              newNode = Node(newBoard,b.getNeighbors(0,newBoard),i,True)
              newNode.counter = counter
              discovered.append(newNode.board)
              queue.append(newNode)
          if done:
            break
        if done:
          break
      for i in queue:
        g.addNewNode(i)

    parent = []
    done = False
    counter = 0
    c = found.counter
    while not done:
      b.printBoard(found.board)
      if found.parent == None:
        print('Cost'': ',c)
        break
      found = found.parent
      counter = counter + 1


  def aMisplaced(self):
    return 0

  def aManhattan(self):
    return 0

  def aGaschnig(self):
    return 0
  
   #g(n) = cost so far to reach n
  def ga(self):
    return 0

  #h(n) = estimated cost from n to goal
  def ha(self):
    return 0

  #f(n) = estimated total cost of path through n to goal
  def fa(self):
    return 0

    def getCoords(index):
      if index in range(0,4):
          X = index
          Y = 0
      elif index in range(3,6):
          X = index - 3
          Y = 1
      elif index in range(6,9):
          X = index - 6
          Y = 2
      return (X,Y) 

    def manhattanDistance(currentBoard, endBoard): # two 1d arrays
        distance = 0
        for i in range(1,9):
            curIndex = currentBoard.index(i)
            endIndex = endBoard.index(i)
            curX, curY = getCoords(curIndex)
            endX, endY = getcoords(endIndex)
            distance += abs(curX - endX) + abs(curY - endY)
        return distance

    def tilesOutOfPlace(currentBoard, endBoard):
        tilesOut = 0
        for i in range(1,9):
            if currentBoard.index(i) != endBoard.index(i):
                tilesOut += 1
        return tilesOut