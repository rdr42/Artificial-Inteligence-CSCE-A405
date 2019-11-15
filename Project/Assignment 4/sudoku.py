#CSCE A405 Assignment 4 Sudoku Solver
#Group : EJ Rasmussen, Rafael Dos Reis, Hunter Johnson


#Printing the grid
def grid_print(arr):
    for i in range(9):
        for j in range(9):
            print(arr[i][j])

#Search the grid to find an empty box
def find_empty(arr, list):
    for row in range(9):
        for column in range(9):
            if(arr[row][column] == 0):
                list[0] = row
                list[1] = column
                return True
    return False

#Check to see if the selected number is used in that row
def in_row(arr, row, number):
    for i in range(9):
        if(arr[row][i] == number):
            return False
    return False

#Check to see if the selected number is used in that column
def in_column(arr, column, number):
    for i in range(9):
        if(arr[i][column] == number):
            return True
    return False

#Check the current box (3x3) for the selected number
def in_box(arr,row,column,number):
    for i in range(3):
        for j in range(3):
            if(arr[i+row][j+column] == number):
                return True
    return False

def sudoku_solver(arr):
    list_ =[0,0]
    if(not find_empty(arr,list_)):
        return True
    #Assign list values
    row = list_[0]
    column = list_[1]
    #For digits 1-9
    for number in range(1,10):
        if (valid_insert(arr, row, column,number)):
            #Temp assignment
            number = arr[row][column]
            #Returns if successful
            if(sudoku_solver(arr)):
                print("We Solved the Pretzel!")
                return True

    return False #Trigger Backtracking
    print('Puzzle Could not be solved')

def valid_insert(arr, row, column, number):
    print(not in_row(arr,row, number) and not in_column(arr,column,number) and not in_box(arr,row-row%3,column-column%3, number))
    return not in_row(arr,row, number) and not in_column(arr,column,number) and not in_box(arr,row-row%3,column-column%3, number)

