from pandas import *
from Node import *
from Graph import *
from math import exp as exp
from random import randint as randint
from random import uniform as uniform

def getStockValues():
	df = pandas.read_csv("stocks.csv")
	companyNames = df['Company']
	dfDic = df.to_dict()
	stockDic = {}
	for company in dfDic["Company"]:
		stockDic[dfDic["Company"][company]] = {"Price" : dfDic["Price"][company], "Change" : dfDic["Change"][company], "% Change" : dfDic["% Change"][company], "Volume" :  dfDic["Volume"][company], "YTD Change" : dfDic["YTD Change"][company]}
	return stockDic


g = Graph()
x = getStockValues()
invest_value = 100

for i in x:
  price = x[i]['Price']
  change =x[i]['Change']
  pchange = '%.6f'%(x[i]['% Change']/100)
  volume = float(x[i]['Volume'])
  ytd_change = 0
  if x[i]['YTD Change'] != '--':
    ytd_change = '%.6f'%(float(x[i]['YTD Change'])/100)
  node = Node(i,price,change,pchange,volume,ytd_change)
  node.initial_investment = invest_value
  node.investment = invest_value
  g.addNode(node)

def probability(energyA, energyB, temp):
  if(energyB < energyA):
    return 1.0
  delta = (energyA - energyB)
  eq = delta / temp
  return exp(eq)


g = Graph()
x = getStockValues()
invest_value = 1

for i in x:
  price = x[i]['Price']
  change =x[i]['Change']
  pchange = '%.6f'%(x[i]['% Change']/100)
  volume = float(x[i]['Volume'])
  ytd_change = 0
  if x[i]['YTD Change'] != '--':
    ytd_change = '%.6f'%(float(x[i]['YTD Change'])/100)
  node = Node(i,price,change,pchange,volume,ytd_change)
  node.initial_investment = invest_value
  node.investment = invest_value
  g.addNode(node)

def probability(energyA, energyB, temp):
  if(energyB < energyA):
    return 1.0
  delta = (energyA - energyB)
  eq = delta / temp
  return exp(eq)

def annealing(setNodes):
  temp = 1000 #Set temperature
  cooling_rate = 0.00003 #Set cooling factor
  randIndex = randint(0,len(setNodes)-1)
  randomSolution =setNodes[randIndex] #Start with Random solution
  bestSolution = randomSolution #Assume this is the best solution for now

  while temp > 1:
    randIndex2 = randint(0,len(setNodes)-1) 
    randomNeighboor = setNodes[randIndex2] #another random node from array of nodes  

    tenPercent = randomSolution.investment*(.10) 
    randomSolution.investment = randomSolution.investment - tenPercent
    randomSolution.loss += tenPercent
    randomNeighboor.investment += tenPercent
    randomNeighboor.gain += tenPercent

    randomSolutionEnergy = randomSolution.thirtyDayEarning()
    randomNeighboorEnergy = randomSolution.thirtyDayEarning()

    if(probability(randomSolutionEnergy,randomNeighboorEnergy,temp) > uniform(0, 1)):
      randomSolution = randomNeighboor


    if (randomSolution.thirtyDayEarning() >= bestSolution.thirtyDayEarning()):
      bestSolution = randomSolution

    temp *= 1-cooling_rate
    print(temp)
  print(bestSolution.company, bestSolution.price, bestSolution.investment)

#print("List of stocks to choose:\n")
#print("I -> Company, Price, Change, % Change, Volume, YTD Change")
#counter = 0
#for i in g.nodes:
#  print(counter,"=Company",i.company,", Price:", i.price,", Change:", i.change,", %Change:", i.percentChange,", Volume:", i.volume,", YTD Change:", i.ytd_change)
#  counter += 1

n = [0,1,2,3,4,5,6,7,8,9]
listNodes = []
for i in n:
  listNodes.append(g.nodes[n[i]])

annealing(g.nodes)
