from sudoku import *
from os import listdir
from os.path import isfile, join
from board import *

fileDirectoryPath = 'sudos/'

#Get all files within sudos directory
fileNames = [f for f in listdir(fileDirectoryPath) if isfile(join(fileDirectoryPath, f))]

sudokuGames = Board()
#Loop through fileNames within fileDirectoryPath and 
for i in fileNames:
    f = open(fileDirectoryPath+i, 'r')
    oneGame = [line.rstrip('\n') for line in f.readlines()]
    f.close()
    node = Node(oneGame)
    node.sanitize()
    sudokuGames.board.append(node)

#Loop through all sudoku games and print their boards
for i in sudokuGames.board:
    i.printBoard()

#Access a sudoku game via i.matrix
for i in sudokuGames.board:
    currentGame = i.matrix
    print(currentGame)
    #Do something with current game