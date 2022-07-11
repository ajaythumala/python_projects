#project sudoku solver - No GUI
#code is currently serving GUI program - no output

board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

#function for solving the board
def solve(Board):
    find = find_empty(Board)
    if not find:
        return True
    else:
        row, col = find

    for num in range(1,10):
        if valid(Board, num, (row,col)):
            Board[row][col] = num

            if solve(Board):
                return True

            Board[row][col] = 0
    return False

#function for checking if the entered value is valid or not
def valid(Board, inp_num, pos_of_num):
    #checking row and col
    for i in range(9):
        if Board[pos_of_num[0]][i] == inp_num and pos_of_num[1] != i:
            return False
        
        if Board[i][pos_of_num[1]] == inp_num and pos_of_num[0] != i:
            return False
    
    #checking inner sqaure
    x_box = (pos_of_num[0] // 3) * 3
    y_box = (pos_of_num[1] // 3) * 3
    for row in range(x_box, x_box + 3):
        for col in range(y_box, y_box + 3):
            if Board[row][col] == inp_num and (row,col) != pos_of_num:
                return False
    
    #all clear if control reaches here
    return True
    

def print_board(Board):
    for row in range(9):
        if row % 3 ==0 and row != 0:
            print("- - - - - - - - - - -")
        for col in range(9):
            if col % 3 == 0 and col != 0 :
                print("|", end = " ")
            if col == 8 :
                print(Board[row][col])
            else:
                print(Board[row][col],end=" ")

#function to find the postion of the next empty space and returns 'None' is none are found
def find_empty(Board):
    for row in range(9):
        for col in range(9):
            if Board[row][col] == 0:
                return row, col
    return None

# test code
# print_board(board)
# print(find_empty(board))
# print(valid(board, 3, (0,2))) #- requires you to change the board value to test
# print(solve(board))

# main code - uncomment to use program
print("Unsolved Board")
print_board(board)

solve(board)

print("\nSolved Board")
print_board(board)
