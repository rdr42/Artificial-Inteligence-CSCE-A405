import numpy as np
from user import *

def generate1DMatrix():
  arr = np.arange(9)
  np.random.shuffle(arr)
  return arr

#Calculates 1-D parity list
def defineParity(a):
  parityList = []
  for i in range(0,9):
    for j in a[i:]:
      if a[i] == 0:
        break
      if a[i] > j and j != 0:
        parityList.append((a[i],j))
  return parityList

def countParity(a):
  return len(a)

def reshape1dTo2D(a):
  b = np.reshape(a,(3, 3))
  return b

def defineLocation(a):
  return np.where(a == 0)

def locationList(a):
  if(a == ([0],[0])):
    return (right,down)
  if(a == ([0],[1])):
    return (left,right,down)
  if(a == ([0],[2])):
    return (left,down)
  if(a == ([1],[0])):
    return (up,right,down)
  if(a == ([1],[1])):
    return (up,right,down,left)
  if(a == ([1],[2])):
    return (up,down,left)
  if(a == ([2],[0])):
    return (up,right)
  if(a == ([2],[1])):
    return (up,right,left)
  if(a == ([2],[2])):
    return (up,left)

def futureLocation(a):
  return (a[0]+currentLocation[0],a[1]+currentLocation[1])

def elementAtLocation(a):
  return newMatrix[a]

#Even is 0, and Odd is 1
def defineParityCongruence(a):
  if a % 2 == 0:
    return 0
  else:
    return 1

right = [0,1]
left = [0,-1]
down = [1,0]
up = [-1,0]
currentLocation = None
matrix = np.array([5,2,8,4,1,7,0,3,6])
newMatrix = reshape1dTo2D(matrix)
defineLocationVariable = defineLocation(newMatrix)
currentLocation = defineLocationVariable
locationListVariable = locationList(defineLocation(newMatrix))
futureLocationVariable = list(map(futureLocation,locationListVariable))
parityList = defineParity(matrix)
parityCount = countParity(parityList)
swappableElements = list(map(elementAtLocation,futureLocationVariable))
parityCongruence = defineParityCongruence(parityCount)
print("Matrix:\n",newMatrix)
print("\nMatrix parity list:\n",parityList)
print("\nMatrix parity count:\n",parityCount)
print("\nMatrix parity congruence:\n",parityCongruence)
print("\nLocation of flag:\n",defineLocationVariable)
print("\nPossible moves:\n",locationListVariable)
print("\nFuture Possible Locations:\n",futureLocationVariable)
print("\nElements to swap with:\n",swappableElements)
print(UserInput.inputConstraints())