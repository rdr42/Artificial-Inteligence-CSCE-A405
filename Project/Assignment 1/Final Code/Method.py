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
  #Flag 3 -- Gaschnig Heuristic

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

  # This is our a* search function, it uses the heuristic functions we've made to make a more informed choice when selecting next nodes.
  # Depending on what value for heuristic you pass in it will calculate the h value by either using:
  # 1: Tiles Out of Place
  # 2: Manhattan Distance
  # 3: Gaschnig
  def aStar(self, heuristic):
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
    if heuristic == 1:
      n.h = self.tilesOutOfPlace(start,end)
    elif heuristic == 2:
      n.h = self.manhattanDistance(start,end)
    elif heuristic == 3:
      n.h = self.gaschnig(start, end)
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

        if heuristic == 1:
          newNode.h = self.tilesOutOfPlace(newBoard,end)
        elif heuristic == 2:
          newNode.h = self.manhattanDistance(newBoard,end)
        elif heuristic == 3:
          newNode.h = self.gaschnig(newBoard, end)
        
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
    # Gaschnig is the last heuristic used, checking for it makes it so we only print the path once
    if heuristic == 3:
      self.displayPath(found,b)

  #Given a board, calculates the total number of misplaced tiles
  def tilesOutOfPlace(self,currentBoard, endBoard):
    tilesOut = 0
    for i in range(1,9):
        if currentBoard.index(i) != endBoard.index(i):
            tilesOut += 1
    return tilesOut

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

  # This function computes the Gaschnig h value for a current board and end board.
  def gaschnig(self, cur, end):
    currentBoard = cur.copy()
    endBoard = end.copy()
    swaps = 0
    done = currentBoard == endBoard
    swapval = -1
    while not done:
      swaps += 1
      # If the blank tile is at the same index in both the current board and the end board and we haven't reached the end board yet
      # need to swap with another arbitrary value
      if currentBoard.index(0) == endBoard.index(0):
        for i in range(1,9):
          # Only swap the blank tile with a tile that isn't where it needs to be. ie if 6 is at the index it needs to be, pick another
          if currentBoard.index(i) != endBoard.index(i):
            # We've found a value we can swap with
            swapval = i
            break
        indexOfBlank = currentBoard.index(0)
        indexOfSwapVal = currentBoard.index(swapval)
        currentBoard[indexOfBlank] = swapval
        currentBoard[indexOfSwapVal] = 0
      # If the blank tile occupies different indicies in the current board and end board then we can swap with the value on the endboard
      # which corresponds to the index the blank tile is in.
      else:
        indexOfBlank = currentBoard.index(0)
        swapval = endBoard[indexOfBlank]
        indexOfSwapVal = currentBoard.index(swapval)
        currentBoard[indexOfBlank] = swapval
        currentBoard[indexOfSwapVal] = 0
      done = currentBoard == endBoard
    return swaps


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