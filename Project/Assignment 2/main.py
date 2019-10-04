from pandas import *
from Node import *
from Graph import *
from math import exp as exp
from random import randint as randint
from random import uniform as uniform
from random import shuffle as shuffle
from random import seed as seed
from copy import copy
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

def getDeltaError(sender, reciever):
	currentValue = sender.investment + sender.investment * sender.percentChange
	currentValue += reciever.investment + reciever.investment * reciever.percentChange
	tempRec = reciever.investment + sender.investment * 0.1
	tempSend = sender.investment - sender.investment * 0.1
	futureValue = tempRec + tempRec * reciever.percentChange
	futureValue += tempSend + tempSend * sender.percentChange
	return futureValue - currentValue


counter = 0
for i in g.nodes:
  print("Stock ID:" ,counter,"| Company Name: ",i.company,", Price:", i.price)
  counter += 1
tfb_choice = input("Enter the Stock IDs followed by a comma and hit enter:\nExample: 1,0,2,9,3,0,4,9,5,1\n").split(",")



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
