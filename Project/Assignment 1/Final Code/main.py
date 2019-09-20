from Heuristic import *
from Board import *

# This function accepts two 1d lists and will return true if the two lists have the same parity
def parity(start, end):
	# Get parity of start state
	startPairs = 0
	for i in range(9):
		for j in range(i+1, 9):
			if start[i] > start[j] and start[i] and start[j]:
				startPairs += 1

	# Get parity of end state
	endPairs = 0
	for i in range(9):
		for j in range(i+1, 9):
			if end[i] > end[j] and end[i] and end[j]:
				endPairs += 1

	# Return if both are even or odd
	return startPairs % 2 == endPairs % 2


# Main function prompts the user for input and then runs the three different search methods
def main():
	print("Input your states with numbers delimited by commas and the blank space represented as a 0")
	print("For example the board:")
	print("[ ,1,2]")
	print("[3,4,5]")
	print("[6,7,8]")
	print("Will be inputted as: 0,1,2,3,4,5,6,7,8")
	
	# Get user input and split into lists of string values
	startBoard = input("\nStart State: ").split(",")
	endBoard =   input("\nEnd State:   ").split(",")
	
	print(len(startBoard), len(endBoard))
	if (len(startBoard) != 9) or (len(endBoard) != 9):
		print("Must enter 9 values for each state, exiting.")
		exit()
	# Convert strings to ints
	for i in range(9):
		startBoard[i] = int(startBoard[i])
		endBoard[i] = int(endBoard[i])
	
	# Check for parity
	if (not parity(startBoard, endBoard)):
		print("Parities don't match")
		return

	# 0 is BFS
	# 1 is Misplaced
	# 2 is Manhattan
	h1 = Heuristic(0, startBoard, endBoard)
	h2 = Heuristic(1, startBoard, endBoard)
	h3 = Heuristic(2, startBoard, endBoard)
	
	print("\nRunning BFS")
	h1.hMethod()
	print("\nRunning Tiles Out of Place")
	h2.hMethod()
	print("\nRunning Manhattan Distance")
	h3.hMethod()


# This calls our main function
main()

#Sample Inputs
#Start: 6,1,3,0,2,4,8,7,5
#End:   1,2,3,8,0,4,7,6,5

#Start: 2,3,1,7,0,8,6,5,4
#End:   1,2,3,8,0,4,7,6,5
