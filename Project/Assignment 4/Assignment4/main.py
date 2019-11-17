from os import listdir
from os.path import isfile, join
from board import *
import time
import csv



fileDirectoryPath = 'sudos/'

#Get all files within sudos directory
fileNames = [f for f in listdir(fileDirectoryPath) if isfile(join(fileDirectoryPath, f))]

sudokuGames = Game()
#Loop through fileNames within fileDirectoryPath and 
for i in fileNames:
    f = open(fileDirectoryPath+i, 'r')
    game = [line.rstrip('\n') for line in f.readlines()]
    game = [line.rstrip('\r') for line in game]
    f.close()
    matrix = Matrix(game)
    matrix.sanitize()
    sudokuGames.board.append(matrix)
    sudokuGames.name = i

print(fileNames.sort())
#All games stored in sudokuGames in sudokGames.board.
counter = 0 
with open('solver.csv', 'w') as csvfile:
  filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
  filewriter.writerow(['Filename', 'Duration'])
  for game in sudokuGames.board:
    start_time = time.time()
    print("\nRunning sudoku solver on: ",fileNames[counter],"\n")
    print("Starting a new sudoku game, good luck !\n")
    aGame = game.matrix
    sudoku = Sudoku(aGame)
    print("Original Board:\n")
    sudoku.printBoard()
    print("Now, solving...")
    if(sudoku.backtrackSolver(sudoku)):
      print("Solved!")
      sudoku.printBoard()
    else:
      print("Unable to solve sudoku.")
    print("Time taken to complete execution:\n ")
    print("--- %s seconds ---" % (time.time() - start_time))
    filewriter.writerow([fileNames[counter], (time.time() - start_time)])

    counter += 1