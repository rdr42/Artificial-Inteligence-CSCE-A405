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

    maxOpenSize = 0

    while len(queue) > 0 and not done:
      if len(queue) > maxOpenSize:
      	maxOpenSize = len(queue)
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

    print("Max size of open list: ", maxOpenSize)
    print("Amount of nodes visited: ", len(discovered))


  def MISP(self):
    # Create the board, the end and start goals and set cost to 0
    b = Board()
    start = self.start
    end = self.goal
    cost= 0

    # Initialize queue list and discovered list
    # Our "queue" is actually just a list that we sort on F values after each time children are added to it.
    queue = []
    discovered = []

    # Create the root Node
    n = Node(start,b.getNeighbors(0,start),False)
    n.parent = None
    n.cost= cost
    n.h = b.tilesOutOfPlace(start,end)
    n.g = cost
    g = Graph()
    g.addNewNode(n)
    queue.append(n)

    # Initialize loop boolean, and a variable to hold the node that is equal to the goal
    done = False
    found = None

    maxOpenSize = 0

    while len(queue) > 0 and not done:
      # Check to see if the current size of our open list is greater than the max size seen so far
      if len(queue) > maxOpenSize:
      	maxOpenSize = len(queue)
      
      # Pop the node with the lowest F value off our list
      v = queue.pop()
      if v.board not in discovered:
        discovered.append(v.board)
      if v.board == end:
        found = v
        break 
      cost = cost + 1
    
      # Create the children for the current nodes and add them to the queue
      for i in v.edge:
        newBoard = b.switchPieces(0,i,v.board)
        newNode = Node(newBoard,b.getNeighbors(0,newBoard),True)
        newNode.parent = v
        # h value is determined by the tiles out of place heuristic
        newNode.h = b.tilesOutOfPlace(newBoard,end)
        newNode.g = self.currentDepth(v) + 1

        if newBoard == end:
          found = newNode
          done = True
          break
        else:
          if newBoard not in discovered and newBoard != start:
            queue.append(newNode)
        if done:
          break

      # New nodes added into our "queue" have made the list out of order, sort the queue 
      queue.sort(key=lambda obj: obj.g + obj.h , reverse=True)
      for i in queue:
        # add the new node into the queue
        g.addNewNode(i)

    print("Max size of open list: ", maxOpenSize)
    print("Amount of nodes visited: ", len(discovered))
    #self.displayPath(found,b)
      

  def MAN(self):
    # Create the board, the end and start goals and set cost to 0
    b = Board()
    start = self.start
    end = self.goal
    cost= 0

    # Initialize queue list and discovered list
    # Our "queue" is actually just a list that we sort on F values after each time children are added to it.
    queue = []
    discovered = []

    # Create the root Node
    n = Node(start,b.getNeighbors(0,start),False)
    n.parent = None
    n.cost= cost
    n.h = self.manhattanDistance(start,end)
    n.g = cost
    g = Graph()
    g.addNewNode(n)
    queue.append(n)

    # Initialize loop boolean, and a variable to hold the node that is equal to the goal
    done = False
    found = None

    maxOpenSize = 0

    while len(queue) > 0 and not done:
      # Check to see if the current size of our open list is greater than the max size seen so far
      if len(queue) > maxOpenSize:
      	maxOpenSize = len(queue)
      
      # Pop the node with the lowest F value off our list
      v = queue.pop()
      if v.board not in discovered:
        # Add the board stsate to our list of previously seen boards
        discovered.append(v.board)
      if v.board == end:
        found = v
        break 
      cost = cost + 1
    
      # Create the children for the current node and add them to the queue
      for i in v.edge:
        newBoard = b.switchPieces(0,i,v.board)
        newNode = Node(newBoard,b.getNeighbors(0,newBoard),True)
        newNode.parent = v
        # h value is determined from Manhattan distance heuristic
        newNode.h = self.manhattanDistance(newBoard,end)
        newNode.g = self.currentDepth(v) + 1
        if newBoard == end:
          found = newNode
          done = True
          break
        else:
          if newBoard not in discovered and newBoard != start:
            # add the new node into the queue
            queue.append(newNode)
        if done:
          break

      # New nodes added into our "queue" have made the list out of order, sort the queue 
      queue.sort(key=lambda obj: obj.g + obj.h , reverse=True)
      for i in queue:
        g.addNewNode(i)

    print("Max size of open list: ", maxOpenSize)
    print("Amount of nodes visited: ", len(discovered))
    self.displayPath(found,b)

  # This function takes two game boards and calculates the Manhattan Distance between them
  def manhattanDistance(self,currentBoard, endBoard):
    distance = 0
    for i in range(1,9):
      curIndex = currentBoard.index(i)
      endIndex = endBoard.index(i)
      curX, curY = self.getCoords(curIndex)
      endX, endY = self.getCoords(endIndex)
      distance += abs(curX - endX) + abs(curY - endY)
    return distance

  # Helper function to return the 2d coordinates of a 1d index.
  def getCoords(self,index):
    if index in range(0,3):
        X = index
        Y = 0
    elif index in range(3,6):
        X = index - 3
        Y = 1
    elif index in range(6,9):
        X = index - 6
        Y = 2
    return X,Y 

  # This function iterates over the parents each node in the solution path and prints their boards
  def displayPath(self,found,b):
    solutionList = []
    done = False
    c = 0
    while not done:
      solutionList.append(found.board)
      if found.parent == None:
        print('Cost'': ',c)
        break
      c = c + 1
      found = found.parent

    solutionList.reverse()
    for i in solutionList:
    	b.printBoard(i)

  # Helper function to get the current depth of a node.
  def currentDepth(self,found):
    done = False
    c = 0
    while not done:
      if found.parent == None:
        return c
        break
      c = c + 1
      found = found.parent
