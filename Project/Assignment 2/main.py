from pandas import *
from Node import *
from Graph import *

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

for i in x:
  price = x[i]['Price']
  change =x[i]['Change']
  pchange = '%.6f'%(x[i]['% Change']/100)
  volume = float(x[i]['Volume'])
  ytd_change = 0
  if x[i]['YTD Change'] != '--':
    ytd_change = '%.6f'%(float(x[i]['YTD Change'])/100)
  g.addNode(Node(i,price,change,pchange,volume,ytd_change))

for i in g.nodes:
  print(i.company,i.price,i.change,i.percentChange, i.volume,i.ytd_change)

	