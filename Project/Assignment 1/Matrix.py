def checkEquality(a,b):
  if a == b:
    return True
  else:
    return False
#Even is 0, and Odd is 1
def countParity(a):
  parityList = []
  for i in range(0,9):
    for j in a[i:]:
      if a[i] == 0:
        break
      if a[i] > j and j != 0:
        parityList.append((a[i],j))
  
  return len(parityList)

#Calculates 1-D parity list
def checkParity(a,b):
  if(countParity(a) % 2 == 0 and countParity(b) % 2 == 0):
    return True
  elif(countParity(a) % 3 == 0 and countParity(b) % 3 == 0):
    return True
  else:
    return False
