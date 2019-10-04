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
invest_value = 0

for i in x:
  price = x[i]['Price']
  change =x[i]['Change']
  pchange = '%.8f'%(x[i]['% Change']/100)
  volume = float(x[i]['Volume'])
  ytd_change = 0
  if x[i]['YTD Change'] != '--':
    ytd_change = '%.8f'%(float(x[i]['YTD Change'])/100)
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
invest_value = 2000

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
  cooling_rate = 0.0003 #Set cooling factor
  randIndex = randint(0,len(setNodes)-1)
  randomSolution =setNodes[randIndex] #Start with Random solution
  bestSolution = randomSolution #Assume this is the best solution for now

  while temp > 1:
    randIndex2 = randint(0,len(setNodes)-1) 
    randomNeighboor = setNodes[randIndex2] #another random node from array of nodes  
    if randomNeighboor.company == randomSolution.company:
      done = False
      while not done:
        randIndex2 = randint(0,len(setNodes)-1) 
        randomNeighboor = setNodes[randIndex2]
        if randomNeighboor.company != randomSolution.company:
          done = True

    tenPercent = randomSolution.investment*(.10) 
    randomSolution.investment -= tenPercent
    randomSolution.loss += tenPercent
    randomNeighboor.investment += tenPercent
    randomNeighboor.gain += tenPercent

    print("SET:")
    randomSolutionEnergy = randomSolution.thirtyDayEarning()
    print("R1: ",randomSolution.company,", Energy:")
    randomNeighboorEnergy = randomSolution.thirtyDayEarning()
    print("R1: ",randomNeighboor.company,", Energy")
    print("SET:")
    if(probability(randomSolutionEnergy,randomNeighboorEnergy,temp) > uniform(0, 1)):
      randomSolution = randomNeighboor


    if (randomSolution.thirtyDayEarning() >= bestSolution.thirtyDayEarning()):
      bestSolution = randomSolution

    temp *= 1-cooling_rate
    #print(temp)
  print("Best Solution:",bestSolution.company,", Total Investement:",bestSolution.investment)
  print("Other investments:\n")
  for i in setNodes:
    if i.company != bestSolution.company:
      print(i.company,", Total Investement:",i.investment)

#print("List of stocks to choose from on:\n")
counter = 0
for i in g.nodes:
  print("Stock ID:" ,counter,"| Company Name: ",i.company,", Price:", i.price)
  counter += 1
tfb_choice = input("Enter the Stock IDs followed by a comma and hit enter:\nExample: 10,0,2,9,3,20,4,19,5,1\n").split(",")

listNodes = []
for i in tfb_choice:
  listNodes.append(g.nodes[int(i)])
annealing(listNodes)
hillclimbing(listNodes)

def getDeltaError(sender, reciever):
	currentValue = sender.investment + sender.investment * sender.percentChange
	currentValue += reciever.investment + reciever.investment * reciever.percentChange
	tempRec = reciever.investment + sender.investment * 0.1
	tempSend = sender.investment - sender.investment * 0.1
	futureValue = tempRec + tempRec * reciever.percentChange
	futureValue += tempSend + tempSend * sender.percentChange
	return futureValue - currentValue


def hillClimbing(nodeList):
	while 