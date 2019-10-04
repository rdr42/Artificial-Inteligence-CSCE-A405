from pandas import *
from Node import *
from Graph import *
from math import exp as exp
from random import randint as randint
from random import uniform as uniform
from random import shuffle as shuffle
from copy import copy as copy
def getStockValues():
	df = pandas.read_csv("stocks.csv")
	companyNames = df['Company']
	dfDic = df.to_dict()
	stockDic = {}
	for company in dfDic["Company"]:
		stockDic[dfDic["Company"][company]] = {"Price" : dfDic["Price"][company], "Change" : dfDic["Change"][company], "% Change" : dfDic["% Change"][company], "Volume" :  dfDic["Volume"][company], "YTD Change" : dfDic["YTD Change"][company]}
	return stockDic



def probability(energyA, energyB, temp):
  if(energyB < energyA):
    return 1.0
  delta = (energyA - energyB)
  eq = delta / temp
  return exp(eq)


g = Graph()
x = getStockValues()
invest_value = 1000

for i in x:
  price = x[i]['Price']
  change =x[i]['Change']
  pchange = float('%.6f'%(x[i]['% Change']/100))
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



def getDeltaError(sender, reciever):
	currentValue = sender.investment + sender.investment * sender.percentChange
	currentValue += reciever.investment + reciever.investment * reciever.percentChange
	tempRec = reciever.investment + sender.investment * 0.1
	tempSend = sender.investment - sender.investment * 0.1
	futureValue = tempRec + tempRec * reciever.percentChange
	futureValue += tempSend + tempSend * sender.percentChange
	return futureValue - currentValue


def hillClimbing(nodeList):
	# Continue until no state is better than the current state
	#companyList = nodeList.copy()
	start = True
	i = 10
	globalMax = (0.0, None)
	while i > 0: 
		newMax = True
		companyList = nodeList.copy()
		if not start:
			totalValue = 10000
			shuffle(companyList)
			for node in companyList:
				if companyList.index(node) == 9 and totalValue > 0:
					node.investment = totalValue
				if totalValue > 0:
					startValueTooLarge = True
					while startValueTooLarge:
						startValue = randint(1, 15) * 100
						startValueTooLarge = startValue > totalValue
					totalValue -= startValue
					node.investment = float(startValue)
				else:
					node.investment = 0.0
		
		while True:
			maxVal = 0
			move = None
			nextState = []
			actualMoves = []
			# For each company check and see if they can swap with another company and increase the value
			for receiver in companyList:
				# Check each node 
				for sender in companyList:
					if sender == receiver:
						continue
					deltaE = getDeltaError(sender, receiver)
					if deltaE > maxVal:
						#print(deltaE)
						maxVal = deltaE
						move = (receiver, sender)
			if move == None or move[1].investment < 0.01:
				sumValue = 0
				for node in companyList:
					sumValue += (node.investment + node.investment * node.percentChange)
				
				if sumValue > globalMax[0]:
					if newMax and not start:
						i += 5
						newMax = False
					globalMaxList = []
					for node in companyList:
						globalMaxList.append(copy(node))
					globalMax = (sumValue, globalMaxList)
				
				i -= 1
				break
			else:
				move[0].investment += (move[1].investment * 0.1)
				move[1].investment -= (move[1].investment * 0.1)
		
		start = False
	return globalMax


#print("List of stocks to choose from on:\n")
counter = 0
for i in g.nodes:
  print("Stock ID:" ,counter,"| Company Name: ",i.company,", Price:", i.price)
  counter += 1
tfb_choice = input("Enter the Stock IDs followed by a comma and hit enter:\nExample: 10,0,2,9,3,20,4,19,5,1\n").split(",")

listNodes = []
for i in tfb_choice:
  print(g.nodes[int(i)].company, g.nodes[int(i)].investment)
  listNodes.append(g.nodes[int(i)])
hillNodes = listNodes.copy()
tfbNodes = listNodes.copy()
#annealing(listNodes)
results = hillClimbing(hillNodes)
print(results[0])
nodes = results[1]
investmentSum = 0
for node in nodes:
	print(node.company, 'Ending value with gain:', "{0:.2f}".format(node.investment))
	investmentSum += node.investment + node.investment * node.percentChange
print('Total sum after hill climbing:', "{0:.2f}".format(investmentSum))
