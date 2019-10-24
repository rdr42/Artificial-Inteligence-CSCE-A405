import math
from datetime import datetime

class Node():
    def __init__(self):
        self.children = {}
        self.board = None
        self.depth = None
        self.player = None
        self.index = None

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

  
  def specialLoop(self, index):
  	if index < 13:
  		return index + 1
  	else:
  		return 0

  # Returns -1 if index is invalid for player
  # Returns 1 if value at index is valid
  # Returns 0 if value at index is 0
  # Returns 100 if player 1 wins
  # Returns 200 if player 2 wins
  def movePiece(self,board,index,player):
    if player == '1':
      if index not in self.op1:
        return -1
      else:
        #get value of index piece
        if board[index] == 0:
          return 0
        else:
          pieceValue = board[self.op1[index]]
          board[index] = 0
          counter = 1
          while pieceValue > 0:
            increment = self.specialLoop(index)
            if increment != 13:
              if self.shouldSteal(pieceValue,increment,player):
               self.stealing(player,increment)
              board[increment] += 1
              pieceValue -= 1
            index = increment
        return 1
    
    if player == '2':
      if index not in self.op2:
        return -1
      else:
        #get value of index piece
        if board[index] == 0:
          return 0
        else:
          pieceValue = board[index]
          board[index] = 0
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

  def gameOver(self, board):
    totalP2 = 0
    for i in board[7:13]:
      totalP2 += i
    if totalP2 == 0:
      return True
    totalP1 = 0
    for i in board[:6]:
      totalP1 += i
    if totalP1 == 0:
      return True
    return False


  def alphaBeta(self,node, a, b):
      alpha = (a, None)
      beta = (b, None)
      if not node.children:
          return (self.heuristic(node.board), node.index)

      # Max
      if node.player == 0:
          for key in node.children:
              val = self.alphaBeta(node.children[key], alpha[0], beta[0])
              if val[0] > alpha[0]:
                  alpha = (val[0], node.children[key].index)
              if alpha[0] >= beta[0]:
                  break
          return alpha
      # Min
      if node.player == 1:
          for key in node.children:
              val = self.alphaBeta(node.children[key], alpha[0], beta[0])
              if val[0] < beta[0]:
                  beta = (val[0], node.children[key].index)
              if beta[0] <= alpha[0]:
                  break
          return beta


  def heuristic(self, board):
    grade = 0
    for i in range(7):
      grade += board[i]
    for i in range(7,14):
      grade -= board[i]

    return grade

  def createTree(self, node):
      possibleMoves = []
      if node.depth == 0 or self.gameOver(node.board):
          return
      if node.player == 0:
        for i in self.op1:
            if node.board[i] != 0:
                possibleMoves.append(i)
      else
        for i in self.op2:
            if node.board[i] != 0:
                possibleMoves.append(i)
      
      for i in possibleMoves:
          childNode = Node()
          childBoard = node.board.copy()
          self.movePiece(childBoard, i, node.player)
          childNode.board = childBoard
          childNode.depth = node.depth - 1
          if node.player == 0:
              childNode.player = 1
          else:
              childNode.player = 0
          node.children[i] = childNode
          node.index = i
          self.createTree(childNode)


  def gameLoop(self):
    depth = 8
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

        node = Node()
        node.board = self.board
        node.depth = depth
        node.player = 0
        before = datetime.now()
        self.createTree(node)
        chooseMove = self.alphaBeta(node, float("-inf"), float("inf"))[1]
        after = datetime.now()
        print("Time taken:", after - before)
        moveError = self.movePiece(self.board, chooseMove,currentPlayer)
        if moveError == -1 or moveError == 0:
          if moveError == -1:
            print('Invalid index, please play again.')
          if moveError == 0:
            print('Invalid index, there is nothing there')
          goodMove = False
          while not goodMove:
            

            node = Node()
            node.board = self.board
            node.depth = depth
            node.player = 0
            before = datetime.now()
            self.createTree(node)
            chooseMove = self.alphaBeta(node, float("-inf"), float("inf"))[1]
            after = datetime.now()
            print(after - before)
            moveError = self.movePiece(self.board, chooseMove,currentPlayer)
            if moveError != -1 and moveError != 0:
              goodMove = True
        print("|| Original Move: ",chooseMove,", Decoded move for other team: ",self.decodeMove(chooseMove)," ||")
        currentPlayer = '2'
      else:
        chooseMove = int(input("Opponent, input options: 7 8 9 10 11 12:\n------------------------------------\n")) #some function takes in current board state
        moveError = self.movePiece(self.board,chooseMove,currentPlayer)
        if moveError == -1 or moveError == 0:
          if moveError == -1:
            print('Invalid index, please play again.')
          if moveError == 0:
            print('Invalid index, there is nothing there')
          goodMove = False
          while not goodMove:
            chooseMove = int(input("Opponent, input options: 7 8 9 10 11 12:\n------------------------------------\n"))
            moveError = self.movePiece(self.board,chooseMove,currentPlayer)
            if moveError != -1 and moveError != 0:
              goodMove = True
        currentPlayer = '1'
       
        if self.gameOver(self.board):
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
    for i in range(7):
      playerOneStones += self.board[i]
    for i in range(7,14):
      playerTwoStones += self.board[i]

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


def main():
	a = Board()
	a.gameLoop()

main()
