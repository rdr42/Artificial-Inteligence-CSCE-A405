from BoardAPI import *
from Matrix import *

board = Board([1,2,3,4,5,6,7,8,0])
matrix = checkParity(board.pieces,[0,1,2,3,4,5,6,7,8])
#Available usage of BoardAPI

#Get piece index
index = board.findPieceIndex(0)

#Get piece info 
pinfo = board.getPieceInfo(2)

#Get neighbor info
neighbor = board.getNeighborInfo(7)

#You can swap elements if they are neighbors
board.switch(1,2)

#Print the board
board.printBoard()

#Get list of possible moves as in [0,1] is right, [1,0] is left...
board.getListOfMoves(4)