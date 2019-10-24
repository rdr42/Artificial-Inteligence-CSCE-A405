import math

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
  def shouldSteal(self,pieceValue,index,player):
    arr = []
    if player == '1':
      arr = self.op1
    else:
      arr = self.op2
    if pieceValue == 1 and self.board[index] == 0 and index in arr:
      return True
    else:
      return False
    
  #Steals the opponents stones opposite to current cup and put them into our cup
  def stealing(self,player,index):
    arr = []
    position = index
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
            increment = self.specialLoop(index)
            if increment != 13:
              if self.shouldSteal(pieceValue,increment,player):
               self.stealing(player,increment)
              self.board[increment] += 1
              pieceValue -= 1
            index = increment
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
            increment = self.specialLoop(index)
            if increment != 6:
              if self.shouldSteal(pieceValue,increment,player):
               self.stealing(player,increment)
              self.board[increment] += 1
              pieceValue -= 1
            index = increment
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


  def heuristic(self):
    grade = 0
    for i in range(7):
      grade += self.board[i]
    for i in range(7,14):
      grade -= self.board[i]

    return grade

  def alphabeta(self):
  	possibleMoves = []
  	for i in self.op1:
  		if self.board[i] != 0:
  			possibleMoves.append(i)
  	
  	for i in possibleMoves:
  		newNode 
  		newBoard = self.board.copy()


class Node():
	def __init__(self):
		self.children = None
		self.board = None
		self.depth = None
		self.max = True

  def gameLoop(self):
    over = False
    self.printBoard()
    bad = True
    if bad:
      while bad:
        currentPlayer = input("Who goes first? Computer or Opponent ? (1 or 2)\n")
        if currentPlayer != '1':
          if currentPlayer != '2':
            print("BAD INPUT. Type 1 for computer or 2 for opponent.")
            bad = True
          else:
            bad = False
        else:
          if currentPlayer != '1':
            print("BAD INPUT. Type 1 for computer or 2 for opponent.")
            bad = True
          else:
            bad = False
    print(" ")
    while not over:
      print("*********************************")
      print(" ")
      self.printBoard()
      print(" ")
      print("*********************************")
      if currentPlayer == '1':
        # DELETE THIS BLOCK WHEN AI STUFF READY
        chooseMove = int(input("Computer goes! Input options: 0 1 2 3 4 5:\n------------------------------------\n")) #some function takes in current board state
        # DELETE THIS BLOCK WHEN AI STUFF READY

        #UNCOMMENT THIS BLOCK WHEN AI FUNCTION READY (Make sure you pass a copy of the board) Also, make sure you pass an integer back too.
        #
        #********************
        #
        #choseMove = somefunction(self.board)
        #
        #********************
        #
        #UNCOMMENT THIS BLOCK WHEN AI FUNCTION READY

        moveError = self.movePiece(chooseMove,currentPlayer)
        if moveError == -1 or moveError == 0:
          if moveError == -1:
            print('Invalid index, please play again.')
          if moveError == 0:
            print('Invalid index, there is nothing there')
          goodMove = False
          while not goodMove:
            # DELETE THIS BLOCK WHEN AI STUFF READY
            chooseMove = int(input("Computer goes! Input options: 0 1 2 3 4 5:\n------------------------------------\n")) #some function takes in current board state
            # DELETE THIS BLOCK WHEN AI STUFF READY

            #UNCOMMENT THIS BLOCK WHEN AI FUNCTION READY (Make sure you pass a copy of the board) Also, make sure you pass an integer back too.
            #
            #********************
            #
            #choseMove = somefunction(self.board)
            #
            #********************
            #
            #UNCOMMENT THIS BLOCK WHEN AI FUNCTION READY

            moveError = self.movePiece(chooseMove,currentPlayer)
            if moveError != -1 and moveError != 0:
              goodMove = True
        print("|| Original Move: ",chooseMove,", Decoded move for other team: ",self.decodeMove(chooseMove)," ||")
        currentPlayer = '2'
      else:
        chooseMove = int(input("Opponent, input options: 7 8 9 10 11 12:\n------------------------------------\n")) #some function takes in current board state
        moveError = self.movePiece(chooseMove,currentPlayer)
        if moveError == -1 or moveError == 0:
          if moveError == -1:
            print('Invalid index, please play again.')
          if moveError == 0:
            print('Invalid index, there is nothing there')
          goodMove = False
          while not goodMove:
            chooseMove = int(input("Opponent, input options: 7 8 9 10 11 12:\n------------------------------------\n"))
            moveError = self.movePiece(chooseMove,currentPlayer)
            if moveError != -1 and moveError != 0:
              goodMove = True
        currentPlayer = '1'
       
        if self.gameOver:
          print("Game is over")
          self.printBoard()
          print(" ")
          score = self.collectStones()
          print("Our Total: ",score[0],", Opponent Total: ",score[1])
          if score[0] > score[1]:
            print("WE WON !!!!!!!!!!!!!!!!!")
          elif score[0] == score[1]:
            print("WE TIED.")
          else:
            print("Opponent won.")
          over = True

  def collectStones(self):
    playerOneStones = 0
    playerTwoStones = 0
    for i in self.board[:6]:
      playerOneStones += i
    
    for j in self.board[7:13]:
      playerTwoStones += j

    return [playerOneStones,playerTwoStones]

  def decodeMove(self,move):
    if move == 0:
      return 7
    if move == 1:
      return 8
    if move == 2:
      return 9
    if move == 3:
      return 10
    if move == 4:
      return 11
    if move == 5:
      return 12


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

#print(c)
