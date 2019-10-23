class Board():
  def __init__(self):
    self.board = [3,3,3,3,3,3,0,3,3,3,3,3,3,0]
    self.op2 = [7,8,9,10,11,12]
    self.op1 = [0,1,2,3,4,5]
  
  def printBoard(self):
    print('  ',self.board[12],self.board[11],self.board[10],self.board[9],self.board[8],self.board[7])
    print(self.board[13],'             ',self.board[6])
    print('  ',self.board[0],self.board[1],self.board[2],self.board[3],self.board[4],self.board[5])

  #Returns true if current player is able to steal stones from opponent's board
  def shouldSteal(self,pieceValue,index,counter,player):
    arr = []
    if player == '1':
      arr = self.op1
    else:
      arr = self.op2
    if pieceValue == 1 and self.board[index+counter] == 0 and index+counter in arr:
      return True
    else:
      return False
    
  #Steals the opponents stones opposite to current cup and put them into our cup
  def stealing(self,player,counter,index):
    arr = []
    position = index + counter
    cupIndex = None
    steal = None
    if player == '1':
      cupIndex = 6
      if position == 0:
        steal = 12
      if position == 1:
        steal = 11
      if position == 2:
        steal = 10
      if position == 3:
        steal = 9
      if position == 4:
        steal = 8
      if position == 5:
        steal = 7
    else:
      cupIndex = 13
      if position == 7:
        steal = 5
      if position == 8:
        steal = 4
      if position == 9:
        steal = 3
      if position == 10:
        steal = 2
      if position == 11:
        steal = 1
      if position == 12:
        steal = 0

    stolenStones = self.board[steal]
    self.board[steal] = 0
    self.board[cupIndex] += stolenStones

  # Returns -1 if index is invalid for player
  # Returns 1 if value at index is valid
  # Returns 0 if value at index is 0
  # Returns 100 if player 1 wins
  # Returns 200 if player 2 wins
  def movePiece(self,index,player):
    if player == '1':
      if index not in self.op1:
        return -1
      else:
        #get value of index piece
        if self.board[index] == 0:
          return 0
        else:
          pieceValue = self.board[self.op1[index]]
          self.board[index] = 0
          counter = 1
          while pieceValue > 0:
            if index+counter != 13:
              #Test 
              if self.shouldSteal(pieceValue,index,counter,player):
                self.stealing(player,counter,index)
              #
              self.board[index+counter] += 1
            counter += 1
            pieceValue -= 1
        return 1
    
    if player == '2':
      if index not in self.op2:
        return -1
      else:
        #get value of index piece
        if self.board[index] == 0:
          return 0
        else:
          pieceValue = self.board[index]
          self.board[index] = 0
          counter = 1
          while pieceValue > 0:
            if index+counter != 6:
              #Test 
              if(self.shouldSteal(pieceValue,index,counter,player)):
                self.stealing(player,counter,index)
              #
              self.board[index+counter] += 1
            counter += 1
            pieceValue -= 1
        return 1

  def gameOver(self):
    totalP2 = 0
    for i in self.board[7:13]:
      totalP2 += i
    if totalP2 == 0:
      return 2
    totalP1 = 0
    for i in self.board[:6]:
      totalP1 += i
    if totalP1 == 0:
      return 1
    return 0
    
##    if [j+=j for j in self.board[7:13]] == 0:
#      return 2
#    if [i+=i for i in self.board[:6]] == 0:
#      return 1

#North Player is '1'
# Moves   12 11 10 9 8 7
# GoalN 13            

#South Player is '2'
# Moves   0  1  2  3  4 5  
# GoalS 6

a = Board()
#hard coded board
a.board = [3,4,3,3,3,0,0,3,3,3,3,3,0,0]
a.printBoard()

c = a.movePiece(1,'1')
print(" ")
print(" ")
a.printBoard()

c = a.movePiece(9,'2')
print(" ")
print(" ")
a.printBoard()

#print(c)