#Amount stock earns over a 30-day period stockEarn
# amount_invested * PGailLoss

#PGainLoss
# (purchase_price - amount_invested)/ purchase_price

#Fitness of a mix over 30-day period
# loss -> if 10% are taken away
# gain -> if 10% are added to your stock
# fitness = sumAll(loss,gain,stocks)


#Move
# r = random stock
# tenPercent = (r.price)*.10
# r.price = r.price - tenPercent
# sendMoneyToRandomStock(tenPercent)
#sampleStock = random.sample(population, 10)

#def probability(energyA, energyB, temp):
#   if(energyB < energyA):
#     return 1.0
#   return Math.exp((energyA - energyB) / temp)

temp = 10000
cooling_rate = 0.003

randomSolution = 0 #random node from array of nodes
bestSolution = randomSolution #Best solution
while temp > 1:
  randomNeighboor = 0 #another random node from array of nodes

  tenPercent = 0 #randomSolution.investment*.10
  #randomSolution.investment = randomSolution.investment - tenPercent
  #randomSolution.loss += tenPercent
  #randomNeighboor.investment += tenPercent
  #randomNeighboor.gain += tenPercent

  randomSolutionEnergy = 0 #randomSolution.initial_investment*pGainLoss
  randomNeighboorEnergy = 0 #randomNeighboor.initial_investment*pGainLoss

  if(probability(randomSolutionEnergy,randomNeighboorEnergy,temp) > random.uniform(0, 1)):
    randomSolution = randomNeighboor


  if (randomSolution.stockEarn < bestSolution.stockEarn) 
    bestSolution = randomSolution
