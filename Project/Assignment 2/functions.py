#Amount a stock earns over a 30-day investment
# Amount of Dolllar invested in some company x
# the percetage loss or gain of some stock.
def cost(dollarInvested,percent):
  return dollarInvested*percent

def randomNeighboor(visited=None,edges=None):
  lenEdges = len(edges)
  import random
  randomIndex = random.randint(0,lenEdges-1)
# If we are accounting for nodes that have already been visited
#  done = False
#  while not done:
#    if edges[randomIndex] not in visited:
#      return edges[randomIndex]
  return edges[randomIndex]

    
def investmentFitness(stocks):
  return 0

