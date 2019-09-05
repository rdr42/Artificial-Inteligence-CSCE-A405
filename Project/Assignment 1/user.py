import numpy as np

class UserInput:
  def __init__(self):
    self.startMatrix = []
    self.goalMatrix = []
    
  def setStartMatrix(self,m):
    self.startMatrix = np.array(m)

  def setGoalMatrix(self,m):
    self.goalMatrix = np.array(m)

  def getGoalMatrix(self):
    return self.goalMatrix
  
  def getStartMatrix(self):
    return self.startMatrix

  def getUserInput():
    userInputVariable = input()

  def inputConstraints():
    message = "\nHow to input matrices:\n Matrix example:\n  |1 2 3|\n  |4 5 6|\n  |7 8 0|\n \n How you will input it:\n [1,2,3,4,5,6,7,8,0] \n Leave 0 as the blank space."
    return message