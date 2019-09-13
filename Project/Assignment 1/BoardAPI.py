class Board:
  #Initialize 3x3 Board
  # 0 is the piece to move
  #:param piece: array of elements to be placed on the board
  #E.g elements: [a, b, c, d, e, f, g, h, i]
  #Indexes:       0  1  2  3  4  5  6  7  8 
  #Matrix Form:  00 01 02 10 11 12 20 21 22
  def __init__(self,piece):
    self.tiles = [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
    self.pieces = piece
    if len(self.pieces) != 9:
      raise Exception('Sorry, only 9 elements are allowed on the board')
    else:
      print('A new board has been initialized.\n')
      print('Current elements on the board: ',self.pieces,'\n')
      self.right = [0,1]
      self.left = [0,-1]
      self.down = [1,0]
      self.up = [-1,0]


  def printBoard(self):
    el = self.pieces
    print(" ------------- ")
    print("||",el[0],"|",el[1],"|",el[2],"||")
    print("")
    print("||",el[3],"|",el[4],"|",el[5],"||")
    print("")
    print("||",el[6],"|",el[7],"|",el[8],"||")
    print(" ------------- ")
  
  #Switch two pieces
  def switch(self,a,b):
    if self.switchable(a,b):
      indexA = self.findPieceIndex(a)
      indexB = self.findPieceIndex(b)
      self.pieces[indexA] = b
      self.pieces[indexB] = a
    else:
      raise Exception("The following items are not neighbors: ", a," and ",b)
    return 0
  
  #Returns true if elements are neighbors, false otherwise
  def switchable(self,a,b):
    if self.getPieceInfo(b) in self.getNeighborInfo(a):
      return True
    else:
      return False

  #Returns your piece, your array index location, your matrix location
  def getPieceInfo(self,a):
    return [a, self.findPieceIndex(a) , self.tileLocation(self.findPieceIndex(a))]

  
  #Return index of piece
  def findPieceIndex(self,a):
    return self.pieces.index(a)
  
  #Return index of tile
  def findTileIndex(self,a):
    return self.tiles.index(a)

#Based on some index, this function returns the location
  #of piece on the imaginary board. e.g 0 would be [0][0]
  def tileLocation(self,index):
    if(index == 0):
      return [0,0]
    if(index == 1):
      return [0,1]
    if(index == 2):
      return [0,2]
    if(index == 3):
      return [1,0]
    if(index == 4):
      return [1,1]
    if(index == 5):
      return [1,2]
    if(index == 6):
      return [2,0]
    if(index == 7):
      return [2,1]
    if(index == 8):
      return [2,2]
  
 #param: element:
 #This function returns the possible moves for current element
  def getListOfMoves(self,element):
    index = self.pieces.index(element)
    if(index == 0):
      return [self.right,self.down]
    if(index == 1):
      return [self.left,self.right,self.down]
    if(index == 2):
      return [self.left,self.down]
    if(index == 3):
      return [self.up,self.right,self.down]
    if(index == 4):
      return [self.up,self.right,self.down,self.left]
    if(index == 5):
      return [self.up,self.down,self.left]
    if(index == 6):
      return [self.up,self.right]
    if(index == 7):
      return [self.up,self.right,self.left]
    if(index == 8):
      return [self.up,self.left]
  
  #Returns neighbor element, neighbor index, and neighbor tile index
  #param:currentLocation: This is your pieceIndex
  #param:possibleMove: Your move index, e.g self.right
  def getNeighbor(self,pieceIndex,possibleMove):
    tileLocation = self.tileLocation(pieceIndex)
    neighborTileIndex = [tileLocation[0]+possibleMove[0],tileLocation[1]+possibleMove[1]]
    neighborIndex = self.findTileIndex(neighborTileIndex)
    neighbor = self.pieces[neighborIndex]
    return [neighbor, neighborIndex, neighborTileIndex]
  
  def getNeighborInfo(self,element):
    moves = self.getListOfMoves(element)
    pindex = self.findPieceIndex(element)
    neighborInfo = []
    for i in moves:
      neighborInfo.append(self.getNeighbor(pindex,i))
    return neighborInfo

  def getProjectedBoard(self,element):
    projectedBoards = []
    for neighbor,x,z in self.getNeighborInfo(element):
      projectedBoards.append(self.projectedSwitch(element,neighbor))
    return projectedBoards

  def projectedSwitch(self,a,b, board = None):
    board = self.pieces.copy()
    if board != None:
      indexA = self.findPieceIndex(a)
      indexB = self.findPieceIndex(b)
      board[indexA] = b
      board[indexB] = a
    return board

  #We are going to associate each neighbor with a transition
  #(0:1,[0,0],[0,1])
