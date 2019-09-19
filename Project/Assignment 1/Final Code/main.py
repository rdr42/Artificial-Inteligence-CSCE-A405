from Heuristic import *
from Board import *

# 0 is BFS
# 1 is Misplaced
# 2 is Manhattam

#h = Heuristic(2,[2,3,1,7,0,8,6,5,4],[1,2,3,8,0,4,7,6,5])

#h.hMethod()


def parity(start, end):
	if len(start) != 9 and len(end) != 9:
		print("Must enter 9 values, exiting.")
		exit()
	startPairs = 0
	for i in range(9):
		for j in range(i+1, 9):
			if start[i] > start[j] and start[i] and start[j]:
				startPairs += 1

	endPairs = 0
	for i in range(9):
		for j in range(i+1, 9):
			if end[i] > end[j] and end[i] and end[j]:
				endPairs += 1

	return startPairs % 2 == endPairs % 2



def main():
	print("Input your states with numbers delimited by commas and the blank space represented as a 0")
	print("For example the board:")
	print("[ ,1,2]")
	print("[3,4,5]")
	print("[6,7,8]")
	print("Will be inputted as: 0,1,2,3,4,5,6,7,8")
	startBoard = input("Start State: ").split(",")
	endBoard = input("End State: ").split(",")
	if (not parity(startBoard, endBoard)):
		return
	heuristic = int(input("Choose the search method (0 for BFS, 1 for A* with Misplaced Tiles, 2 for A* with Manhattan Distance: "))
	if heuristic not in range(3):
		print("Must choose between 0-2 for heuristic, exiting.")
	for i in range(9):
		startBoard[i] = int(startBoard[i])
		endBoard[i] = int(endBoard[i])
	h = Heuristic(heuristic, startBoard, endBoard)
	h.hMethod()


main()