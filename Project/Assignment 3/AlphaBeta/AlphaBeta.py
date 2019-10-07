def minimax_ab(N,A,B):
  N.alpha = A
  N.beta = B
  #print("Went in, alpha: ",A,",beta:",B,"NODE:",N.name)
  if N.isLeaf:
   # print("In Leaf:",N.value)
    return N.value
  elif N.isMin:
    #print("Is Min:")
    for i in N.edges:
     # print("Get MinMax:")
      val = minimax_ab(i, N.alpha, N.beta)
      #print("in MIN i:",i,"N.alpha",N.alpha,"N.beta",N.beta,"VAL:",val)
      N.beta = min(N.beta, val)
      #print("New beta:",N.beta)
      if N.beta <= N.alpha:
        break
    return N.beta
  else:
    #print("Is Max:")
    for i in N.edges:
     # print("Get MinMax:")
      val = minimax_ab(i, N.alpha, N.beta)
      #print("in MAX i:",i,"N.alpha",N.alpha,"N.beta",N.beta,"VAL:",val)
      N.alpha = max(N.alpha, val)
      #print("New alpha:",N.alpha)
      if N.alpha >= N.beta:
        break
    return N.alpha