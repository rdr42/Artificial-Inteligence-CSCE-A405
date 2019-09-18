from Node import *
from Graph import *
from Board import *

class Method: 
  def __init__(self,start,goal):
    self.start = start
    self.goal = goal
    
  #Flag 0 -- Breadth First Search
  #Flag 1 -- Misplaced Tiles Heuristic
  #Flag 2 -- Manhattan Distance Heuristic
  #Flag 3 -- Ganlish Heuristic

  def BFS(self):
    #Create the board, the end and start goals and set cost to 0
    b = Board()
    start = self.start
    end = self.goal
    cost= 0

    #Initialize queue list and discovered list
    queue = []
    discovered = []

    #Create the root Node
    n = Node(start,b.getNeighbors(0,start),False)
    n.parent = None
    n.cost= cost
    g = Graph()
    g.addNewNode(n)
    queue.append(n)

    #Initialize loop boolean, and a variable to hold the node that is equal to the goal
    done = False
    found = None

    while len(queue) > 0 and not done:
      v = queue.pop()
      if v.board not in discovered:
        discovered.append(v.board)

      if v.board == end:
        found = v
        break
      cost+= 1
      for i in g.nodes:
        for j in i.edge:
          newBoard = b.switchPieces(0,j,i.board)
          newNode = Node(newBoard,b.getNeighbors(0,newBoard),True)
          newNode.parent = i
          newNode.cost = cost
          if newBoard == end:
            found = newNode
            done = True
            break
          else:
            if newBoard not in discovered and newBoard != start:
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
    c = found.cost
    while not done:
      b.printBoard(found.board)
      if found.parent == None:
        print('Cost'': ',c)
        break
      found = found.parent

  def MISP(self):
    #Create the board, the end and start goals and set cost to 0
    b = Board()
    start = self.start
    end = self.goal
    cost= 0

    #Initialize queue list and discovered list
    queue = []
    discovered = []

    #Create the root Node
    n = Node(start,b.getNeighbors(0,start),False)
    n.parent = None
    n.cost= cost
    n.h = b.tilesOutOfPlace(start,end)
    n.g = cost
    g = Graph()
    g.addNewNode(n)
    queue.append(n)

    #Initialize loop boolean, and a variable to hold the node that is equal to the goal
    done = False
    found = None

    while len(queue) > 0 and not done:
      v = queue.pop()
      if v.board not in discovered:
        discovered.append(v.board)
      if v.board == end:
        found = v
        break 
      cost = cost + 1
    
      for i in v.edge:
        newBoard = b.switchPieces(0,i,v.board)
        newNode = Node(newBoard,b.getNeighbors(0,newBoard),True)
        newNode.parent = v
        newNode.h = b.tilesOutOfPlace(newBoard,end)
        newNode.g = self.currentDepth(v)

        if newBoard == end:
          found = newNode
          done = True
          break
        else:
          if newBoard not in discovered and newBoard != start:
            if(v.h + v.g <= newNode.h + newNode.g):
              queue.append(newNode)
        if done:
          break

      queue.sort(key=lambda obj: obj.g + obj.h , reverse=True)
      for i in queue:
        g.addNewNode(i)

    self.displayPath(found,b)
      

  def MAN(self):
    #Create the board, the end and start goals and set cost to 0
    b = Board()
    start = self.start
    end = self.goal
    cost= 0

    #Initialize queue list and discovered list
    queue = []
    discovered = []

    #Create the root Node
    n = Node(start,b.getNeighbors(0,start),False)
    n.parent = None
    n.cost= cost
    n.h = self.manhattanDistance(start,end)
    n.g = cost
    g = Graph()
    g.addNewNode(n)
    queue.append(n)

    #Initialize loop boolean, and a variable to hold the node that is equal to the goal
    done = False
    found = None

    while len(queue) > 0 and not done:
      v = queue.pop()
      if v.board not in discovered:
        discovered.append(v.board)
      if v.board == end:
        print('FOUND')
        found = v
        break 
      cost = cost + 1
    
      for i in v.edge:
        newBoard = b.switchPieces(0,i,v.board)
        newNode = Node(newBoard,b.getNeighbors(0,newBoard),True)
        newNode.parent = v
        newNode.h = self.manhattanDistance(newBoard,end)
        newNode.g = self.currentDepth(v)
        if newBoard == end:
          print('FOUND')
          found = newNode
          done = True
          break
        else:
          if newBoard not in discovered and newBoard != start:
            if(v.h + v.g <= newNode.h + newNode.g):
              queue.append(newNode)
        if done:
          break

      queue.sort(key=lambda obj: obj.g + obj.h , reverse=True)
      for i in queue:
        g.addNewNode(i)

  def manhattanDistance(self,currentBoard, endBoard): # two 1d arrays
    distance = 0
    for i in range(1,9):
      curIndex = currentBoard.index(i)
      endIndex = endBoard.index(i)
      curX, curY = self.getCoords(curIndex)
      endX, endY = self.getCoords(endIndex)
      distance += abs(curX - endX) + abs(curY - endY)
    return distance

  def getCoords(self,index):
    if index in range(0,4):
        X = index
        Y = 0
    elif index in range(3,6):
        X = index - 3
        Y = 1
    elif index in range(6,9):
        X = index - 6
        Y = 2
    return X,Y 

  def displayPath(self,found,b):
    parent = []
    done = False
    c = 0
    while not done:
      b.printBoard(found.board)
      if found.parent == None:
        print('Cost'': ',c)
        break
      c = c + 1
      found = found.parent

  def currentDepth(self,found):
    done = False
    c = 0
    while not done:
      if found.parent == None:
        return c
        break
      c = c + 1
      found = found.parent
