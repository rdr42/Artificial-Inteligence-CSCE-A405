from pandas import *
from Node import *
from Graph import *
from math import exp as exp
from random import randint as randint
from random import uniform as uniform
from random import shuffle as shuffle
from random import seed as seed
from copy import copy


def annealing(setNodes):
  temp = 1000000 #Set temperature
  cooling_rate = 0.00003 #Set cooling factor
  counter = 0
  while temp > 1:
    randIndex = randint(0,len(setNodes)-1)
    S1 = setNodes[randIndex]
    randIndex2 = randint(0,len(setNodes)-1) 
    S2 = setNodes[randIndex2] #another random node from array of nodes  
    if S1.company == S2.company:
      done = False
      while not done:
        randIndex2 = randint(0,len(setNodes)-1) 
        S2 = setNodes[randIndex2]
        if S2.company != S1.company:
          done = True
    tempS1 = Node(S1.company,S1.price,S1.change,S1.percentChange,S1.volume,S1.ytd_change)
    tempS1.investment = S1.investment
    tempS2 = Node(S2.company,S2.price,S2.change,S2.percentChange,S2.volume,S2.ytd_change)
    tempS2.investment = S2.investment
    if (getDeltaError(tempS1,tempS2)>0):
      S2.investment += S1.investment *(.1)
      S1.investment -= S1.investment *(.1)
    else:
      if(exp(getDeltaError(tempS1,tempS2)/temp) > uniform(0, 1)):
        S2.investment += S1.investment *(.1)
        S1.investment -= S1.investment *(.1)
    temp *= (1-cooling_rate)
  suma = 0
  for i in setNodes:
      print(i.company,", Total Investement:",i.investment)
      suma+=i.investment*(i.percentChange) + i.investment
  print("Simulated Annealing final result: ",suma)