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

listNodes = []
for i in tfb_choice:
  listNodes.append(g.nodes[int(i)])
annealing(listNodes)
hillclimbing(listNodes)


 