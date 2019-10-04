# Assignment 2
# Node.py
# EJ, Rafael, Hunter

class Node:
  def __init__(self,company,price,change,pChange,volume,ytd_change):
    self.company = company
    self.price = price
    self.change = change
    self.percentChange = pChange
    self.volume = volume
    self.ytd_change = ytd_change
    self.investment = 0
    self.initial_investment = 0
    self.loss = 0
    self.gain = 0

  def updateLoss(self,loss):
    self.loss += loss
  
  def updateGain(self,gain):
    self.gain += gain
  
  def initialInvestment(self,a):
    self.initial_investment = a
  
  def investment(self,a):
    self.investment = a

#Should the amount invested be the intial amount invested on all companies initially? Or
#should it be the amount of the investment at some time i?
  def thirtyDayEarning(self):
   # pGainLoss = self.price - self.investment
   # pGainLoss = pGainLoss / self.price
    return self.investment * float(self.percentChange)


