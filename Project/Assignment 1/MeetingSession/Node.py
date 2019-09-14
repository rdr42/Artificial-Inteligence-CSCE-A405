from Board import *
class Node:
  def __init__(self):
    self.parent = None
    self.parentdirection = None
    self.children = {} #Store node objects{up or left or down or right: node}
    self.value = board #[0,1,2,3,4,4,5]

  def populateChildren(self):
    index = self.value.blank
    if(index == 0):
      if (self.parentdirection != 'r'):
        rightpieces = self.value.pieces
        temp = rightpieces[0]
        rightpieces[0] = rightpieces[1]
        rightpieces[1] = temp
        self.children.update({'r':Node(Board(rightpieces))})
      if (self.parentdirection != 'd'):
        downpieces = self.value.pieces
        temp = downpieces[0]
        downpieces[0] = downpieces[3]
        downpieces[3] = temp
        self.children.update({'r':Node(Board(downpieces))})
    elif(index == 1):
      if (self.parentdirection != 'r'):
        rightpieces = self.value.pieces
        temp = rightpieces[1]
        rightpieces[1] = rightpieces[2]
        rightpieces[2] = temp
        self.children.update({'r':Node(Board(rightpieces))})
      if (self.parentdirection != 'd'):
        downpieces = self.value.pieces
        temp = downpieces[1]
        downpieces[1] = downpieces[4]
        downpieces[4] = temp
        self.children.update({'r':Node(Board(downpieces))})
      if (self.parentdirection != 'l'):
        leftpieces = self.value.pieces
        temp = downpieces[1]
        leftpieces[1] = downpieces[0]
        leftpieces[0] = temp
        self.children.update({'r':Node(Board(leftpieces))})
    elif(index == 2):
      if (self.parentdirection != 'l'):
        leftpieces = self.value.pieces
        temp = downpieces[2]
        leftpieces[2] = downpieces[1]
        leftpieces[1] = temp
        self.children.update({'r':Node(Board(leftpieces))})
      if (self.parentdirection != 'd'):
        downpieces = self.value.pieces
        temp = downpieces[2]
        downpieces[2] = downpieces[5]
        downpieces[5] = temp
        self.children.update({'r':Node(Board(downpieces))})
    elif(index == 3):
      if (self.parentdirection != 'u'):
        uppieces = self.value.pieces
        temp = uppieces[3]
        uppieces[3] = uppieces[0]
        uppieces[0] = temp
        self.children['u'] = Node(Board(uppieces))
      if (self.parentdirection != 'r'):
        rightpieces = self.value.pieces
        temp = rightpieces[3]
        rightpieces[3] = rightpieces[4]
        rightpieces[4] = temp
        self.children['r'] = Node(Board(rightpieces))
      if (self.parentdirection != 'd'):
        downpieces = self.value.pieces
        temp = downpieces[3]
        downpieces[3] = downpieces[6]
        downpieces[6] = temp
        self.children['d'] = Node(Board(downpieces))
    elif(index == 4):
      if (self.parentdirection != 'u'):
        uppieces = self.value.pieces
        temp = uppieces[4]
        uppieces[4] = uppieces[1]
        uppieces[1] = temp
        self.children['u'] = Node(Board(uppieces))
      if (self.parentdirection != 'r'):
        rightpieces = self.value.pieces
        temp = rightpieces[4]
        rightpieces[4] = rightpieces[5]
        rightpieces[5] = temp
        self.children['r'] = Node(Board(rightpieces))
      if (self.parentdirection != 'd'):
        downpieces = self.value.pieces
        temp = downpieces[4]
        downpieces[4] = downpieces[7]
        downpieces[7] = temp
        self.children['d'] = Node(Board(downpieces))
      if (self.parentdirection != 'l'):
        leftpieces = self.value.pieces
        temp = downpieces[4]
        leftpieces[4] = downpieces[3]
        leftpieces[3] = temp
        self.children.update({'r':Node(Board(leftpieces))})
    elif(index == 5):
      if (self.parentdirection != 'u'):
        uppieces = self.value.pieces
        temp = uppieces[5]
        uppieces[5] = uppieces[2]
        uppieces[2] = temp
        self.children['u'] = Node(Board(uppieces))
      if (self.parentdirection != 'd'):
        downpieces = self.value.pieces
        temp = downpieces[5]
        downpieces[5] = downpieces[8]
        downpieces[8] = temp
        self.children['d'] = Node(Board(downpieces))
      if (self.parentdirection != 'l'):
        leftpieces = self.value.pieces
        temp = downpieces[5]
        leftpieces[5] = downpieces[4]
        leftpieces[4] = temp
        self.children.update({'r':Node(Board(leftpieces))})
    elif(index == 6):
      if (self.parentdirection != 'u'):
        uppieces = self.value.pieces
        temp = uppieces[6]
        uppieces[6] = uppieces[3]
        uppieces[3] = temp
        self.children['u'] = Node(Board(uppieces))
      if (self.parentdirection != 'r'):
        rightpieces = self.value.pieces
        temp = rightpieces[6]
        rightpieces[6] = rightpieces[7]
        rightpieces[7] = temp
        self.children['r'] = Node(Board(rightpieces))
    elif(index == 7):
      if (self.parentdirection != 'u'):
        uppieces = self.value.pieces
        temp = uppieces[7]
        uppieces[7] = uppieces[4]
        uppieces[4] = temp
        self.children['u'] = Node(Board(uppieces))
      if (self.parentdirection != 'r'):
        rightpieces = self.value.pieces
        temp = rightpieces[7]
        rightpieces[7] = rightpieces[8]
        rightpieces[8] = temp
        self.children['r'] = Node(Board(rightpieces))
      if (self.parentdirection != 'l'):
        leftpieces = self.value.pieces
        temp = downpieces[7]
        leftpieces[7] = downpieces[6]
        leftpieces[6] = temp
        self.children.update({'r':Node(Board(leftpieces))})
    elif(index == 8):
      if (self.parentdirection != 'u'):
        uppieces = self.value.pieces
        temp = uppieces[8]
        uppieces[8] = uppieces[5]
        uppieces[5] = temp
        self.children['u'] = Node(Board(uppieces))
      if (self.parentdirection != 'l'):
        leftpieces = self.value.pieces
        temp = downpieces[8]
        leftpieces[8] = downpieces[7]
        leftpieces[7] = temp
        self.children.update({'r':Node(Board(leftpieces))})

