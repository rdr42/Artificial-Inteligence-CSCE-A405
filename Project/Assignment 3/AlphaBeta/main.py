from Node import *
from Graph import *
from AlphaBeta import *

a = Node()
a.name = 'A'
a.isMax = True

b = Node()
b.name = 'B'
b.isMin = True

c = Node()
c.name = 'C'
c.isMax = True

d = Node()
d.name = 'D'
d.isMin = True

e = Node()
e.name = 'E'
e.value = 3
e.isLeaf = True

f = Node()
f.name = 'F'
f.value = 48
e.isLeaf = True

g = Node()
g.name = 'G'
g.isMin = True

h = Node()
h.name = 'H'
h.value = 1
h.isLeaf = True

i = Node()
i.name = 'I'
i.isLeaf = True
i.value = 4

j = Node()
j.name = 'J'
j.isMax = True

k = Node()
k.name = 'K'
k.isMin = True

l = Node()
l.name = 'L'
l.isLeaf = True
l.value = 2

m = Node()
m.name = 'M'
m.isLeaf = True
m.value = 25

n = Node()
n.name = 'N'
n.isMin = True

o = Node()
o.name = 'O'
o.isLeaf = True
o.value = 2

p = Node()
p.name = 'P'
p.isLeaf = True
p.value = 11

### Otherside leaf down

t = Node()
t.name = 'T'
t.isLeaf = True
t.value = 12

u = Node()
u.name = 'U'
u.isLeaf = True
u.value = 13

w = Node()
w.name = 'W'
w.isLeaf = True
w.value = 6

x = Node()
x.name = 'X'
x.isLeaf = True
x.value = 8

z2 = Node()
z2.name = 'Z2'
z2.isLeaf = True
z2.value = 19

z3 = Node()
z3.name = 'Z3'
z3.isLeaf = True
z3.value = 17

z5 = Node()
z5.name = 'Z5'
z5.isLeaf = True
z5.value = 15

z6 = Node()
z6.name = 'Z6'
z6.isLeaf = True
z6.value = 11
## leafs up

s = Node()
s.name = 'S'
s.isMin = True

v = Node()
v.name = 'V'
v.isMin = True


z1 = Node()
z1.name = 'Z1'
z1.isMin = True

z4 = Node()
z4.name = 'Z4'
z4.isMin = True

###

r = Node()
r.name = 'R'
r.isMax = True



y = Node()
y.name = 'Y'
y.isMax = True


q = Node()
q.name = 'Q'
q.isMin = True



#####edges

a.edges.append(b)
a.edges.append(q)

b.edges.append(c)
b.edges.append(j)

c.edges.append(d)
c.edges.append(g)

d.edges.append(e)
d.edges.append(f)

g.edges.append(h)
g.edges.append(i)

k.edges.append(l)
k.edges.append(m)

n.edges.append(o)
n.edges.append(p)

j.edges.append(k)
j.edges.append(n)
###################
q.edges.append(r)
q.edges.append(y)

r.edges.append(s)
r.edges.append(v)

y.edges.append(z1)
y.edges.append(z4)

s.edges.append(t)
s.edges.append(u)

v.edges.append(w)
v.edges.append(x)

z1.edges.append(z2)
z1.edges.append(z3)

z4.edges.append(z5)
z4.edges.append(z6)


q = minimax_ab(a,float("-inf"),float("inf"))
print(q)