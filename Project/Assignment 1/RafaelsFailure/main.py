class Node:
  def __init__(self, value, edges):
    self.value = value
    self.edges = edges
    self.board = []
    self.searched = None
    self.parent = None

class Graph:
  def __init__(self):
    self.nodes = []
    self.graph = None

  def addNewNode(self,Node):
    self.nodes.append(Node)

from BoardAPI import *

board = Board([0,1,3,4,2,5,7,8,6])
#Available usage of BoardAPI
g = Graph()

for i in board.pieces:
  neighbor = board.getNeighborInfo(i)
  n = Node(i,neighbor)
  n.board.append(board.getProjectedBoard(i))
  g.addNewNode(n)

start = [0,1,3,4,2,5,7,8,6]

goal = [1,2,3,4,5,6,7,8,0]

discovered = []
queue = []

discovered.append(start)
queue.append(start)

while len(queue) > 0:
  v = queue.pop()
  if v == goal:
    print(v)
#  else:
#    print(g.nodes[0].edges)
#    for i in g.nodes:
#      for j in i.edges:
#        if j in listOfAd
    #for all edges from v to w in G.adjacentEdges(v) do
      #if w is not labeled as discovered:
      #label w as discovered
      #w.parent = v
      #Q.enqueue(w) 

board.getProjectedBoard(1)
print(g.nodes[1].edges)
print(g.nodes[0].board)

v = {(1,(0,1)):[1,2,3,4,5,6],(1,(0,1)):[1,2,3,4,5,6]}
for i in v:
  if i == (1,(0,1)):
    print(v[i])

x = {(0,1):[[0,0],[0,1],[1,2,3,4,5]]}
#x = {(FROM,TO)}
# parent