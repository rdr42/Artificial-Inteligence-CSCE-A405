class Board:
  def __init__(self, pieces):
    self.piece = pieces
    self.blank = self.piece.index(0)
  
  def printBoard(self):
    el = self.piece
    print(" ------------- ")
    print("||",el[0],"|",el[1],"|",el[2],"||")
    print("")
    print("||",el[3],"|",el[4],"|",el[5],"||")
    print("")
    print("||",el[6],"|",el[7],"|",el[8],"||")
    print(" ------------- ")



    