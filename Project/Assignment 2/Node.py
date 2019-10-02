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
