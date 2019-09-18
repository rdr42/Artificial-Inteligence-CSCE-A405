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
  
  #Given a board, prints all elements of a board
  def printBoard(self,board):
    el = board
    print(" ------------- ")
    print("||",el[0],"|",el[1],"|",el[2],"||")
    print("")
    print("||",el[3],"|",el[4],"|",el[5],"||")
    print("")
    print("||",el[6],"|",el[7],"|",el[8],"||")
    print(" ------------- ")
  
  #Given a board, calculates the total number of misplaced tiles
  def tilesOutOfPlace(self,currentBoard, endBoard):
    tilesOut = 0
    for i in range(1,9):
        if currentBoard.index(i) != endBoard.index(i):
            tilesOut += 1
    return tilesOut
