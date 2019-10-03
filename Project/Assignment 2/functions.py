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

def probability(energyA, energyB, temp):
   if(energyB < energyA):
     return 1.0
   return Math.exp((energyA - energyB) / temp)
