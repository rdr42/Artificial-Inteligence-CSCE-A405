
static = [[0,1,2],
          [3,4,5],
          [6,7,8]]
#([0,child],[myposition,futureposition])

#History is appended to current node

#From 0 to 1 ([0,1],[[0][0],[0][1]])
  # New location --> [0][1]
  #                         [[1,0,2],
  #                          [3,4,5],
  #                          [6,7,8]]
  #
  #From 0 to 2 ([0,2],[[0][1],[0][2]])
  #From 0 to 4 ([0,4],[[0][1],[1][1]])
  #From 0 to 1 ([0,1],[[0][1],[0][0]]) Can't go here X

#From 0 to 3 ([0,3],[[0][0],[1][0]])
