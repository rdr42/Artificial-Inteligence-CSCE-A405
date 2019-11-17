import copy

class Matrix:
  def __init__(self,node):
    self.board = node
    self.matrix = None

  #Parsing input from files to a readable 9x9 matrix.
  def sanitize(self):
    matrix = []
    temp = []
    for i in self.board:
      for j in i:
        if j in [str(num) for num in range(10)]:
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

class Game:
  def __init__(self):
    self.board = []
    self.name = ''

class Sudoku:
  def __init__(self,board):
    self.board = board
    self.row = [i for i in range(9)]
    self.col = [j for j in range(9)]
    self.possibleEntries = []

  #Check if piece has duplicate on piece row
  def hasDuplicateOnRow(self,location,element):
    row,column = location
    pieceOnRow = False
    pieces = self.board[row]
    #Check all elements in the row
    for piece in pieces:
      if piece == element:
        pieceOnRow = True
        break
    return pieceOnRow

  #Check if piece has duplicate on piece column
  def hasDuplicateOnCol(self,location, element):
    row,column = location
    pieceOnCol = False

    #Check all elements in a column for each row
    for pieces in self.board:
      if pieces[column] == element:
        pieceOnCol = True
        break
    return pieceOnCol

  #Add a piece to a (x,y) location on board
  #Return 0 if successful entry
  #Return -1 if failed entry
  def addPiece(self,piece,location):
    row,column = location
    if self.validEntry(row,column,piece):
      self.board[row][column] = piece
      return 0
    return -1
      
  #Check if location of adding a piece is valid. It is valid if location is empty.
  def validEntry(self,row,column,piece):
    isValidEntry = True
    if self.board[row][column] != 0:
      return False
    if not self.validBox(row,column,piece):
      return False
    if self.hasDuplicateOnCol((row,column),piece):
      return False
    if self.hasDuplicateOnRow((row,column),piece):
      return False
    return isValidEntry
  
  #Check if 3x3 box is valid
  def validBox(self,row,column,piece):
    x = row-(row%3)
    y = column-(column%3)
    loc = [(x,y),(x,y+1),(x,y+2),(x+1,y),(x+1,y+2),(x+2,y),(x+2,y+1),(x+2,y+2)]
    for x,y in loc:
      if(self.board[x][y] != 0):
          if(self.board[x][y]  == piece):
            return False
    return True
  #Use get board to get a copy of the board
  def getBoard(self):
    board = copy.deepcopy(self.board)
    return board

  def printBoard(self):
    print(' -------------------------')
    print(self.board[0])
    print(self.board[1])
    print(self.board[2])
    print(self.board[3])
    print(self.board[4])
    print(self.board[5])
    print(self.board[6])
    print(self.board[7])
    print(self.board[8])
    print(' -------------------------')

  #Return a list of (x,y) empty locations
  def getEmptyLocation(self):
    possibleEntries = []
    for i in self.row:
      for j in self.col:
        if self.board[i][j] == 0:
          possibleEntries.append((i,j))
    return possibleEntries

  #Check for each possible location
  #If it is not empty 
  def allValid(self):
    allValid = True
    for i in self.board:
      for j in i:
        if j == 0:
          allValid = False
          break
    return allValid

  def backtrackSolver(self,board):
    if board.allValid():
      return True

    empty = board.getEmptyLocation()
    row, col = empty[0]

    #Possible entry values in the domain 1 through 9
    possibleValues = [1,2,3,4,5,6,7,8,9]

    for piece in possibleValues:
      if(board.validEntry(row,col,piece)):
        board.board[row][col] = piece
        if(self.backtrackSolver(board)):
          return True
        board.board[row][col] = 0

    return False

def allPossibleLocations():
  loc = []
  for i in range(9):
    for j in range(9):
      loc.append((i,j))
  return loc

