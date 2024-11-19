import pyautogui as pg
import numpy as np
pygame.font.init()
window = pygame.display.set_mode((500,500))
pygame.display.set_caption(" Sudoku Game By Marni")
x=0
z=0
diff = 500/16
value=0 

# Function to check if it's safe to place a number in a given cell
def is_safe(board, row, col, num):
    # Check if the number is in the row
    for x in range(16):
        if board[row][x] == num:
            return False

    # Check if the number is in the column
    for x in range(16):
        if board[x][col] == num:
            return False

    # Check if the number is in the 4x4 sub-grid
    start_row, start_col = 4 * (row // 4), 4 * (col // 4)
    for i in range(4):
        for j in range(4):
            if board[i + start_row][j + start_col] == num:
                return False

    return True

# Function to solve the 16x16 Sudoku board using backtracking
def solve_sudoku(board):
    empty_location = find_empty_location(board)
    if not empty_location:
        return True  # Puzzle solved

    row, col = empty_location


    for num in range(1, 17):
        if is_safe(board, row, col, num):
            board[row][col] = num

            # Recursively attempt to solve the board
            if solve_sudoku(board):
                return True

            # Undo the move if it doesn't lead to a solution
            board[row][col] = 0

    return False  # Trigger backtracking

# Function to find an empty cell (denoted by 0)
def find_empty_location(board):
    for i in range(16):
        for j in range(16):
            if board[i][j] == 0:
                return (i, j)
    return None

# Function to print the Sudoku board
def print_board(board):
    for row in board:
        print(" ".join(str(hex(num)[2:]).upper() if num > 16 else str(num) for num in row))

# Example 16x16 Sudoku puzzle (0 represents empty cells)
board = [
 [0,  0,  0,  0,  2,  0,  0,  6,  0, 15,  0,  0,  7,  0, 11,  0],
    [5,  0,  0,  9,  0,  0,  0,  8,  0,  0,  0,  4,  0, 10,  0,  0],
    [0,  0,  0,  0,  0, 14,  0,  0, 12,  0,  0,  0,  0,  1,  0,  0],
    [0,  0,  0,  0, 13,  0,  0,  0,  0,  5, 10,  0,  0,  0,  0,  0],
    [12,  0,  0,  0,  0,  5,  0,  4,  0,  0,  0,  1, 14,  0,  0,  0],
    [0,  0,  1,  0,  0,  0,  9,  0,  0,  0,  0, 13,  0,  0,  0,  0],
    [14,  6,  0,  0,  0,  0,  0,  0,  0,  0,  2,  0, 12,  0,  0,  0],
    [0,  0,  0, 11,  0,  0,  0,  0,  0,  0,  0,  0,  0, 15,  0,  0],
    [0,  0,  0, 12,  0,  0,  0,  0,  0,  0,  0, 14,  0,  0,  0,  0],
    [0,  0,  4,  0,  8,  0,  0,  0,  0,  0,  0,  0,  0,  9,  2,  6],
    [0,  0,  7,  0,  0,  1,  0,  0,  0,  0,  0, 10,  0,  0,  0,  4],
    [0,  0,  0,  0,  0,  0,  0, 12,  0,  0,  0,  0,  0,  0,  0,  5],
    [0,  0, 15,  0,  0,  0,  5,  0,  9,  0,  0,  0,  0,  0,  0, 13],
    [0, 13,  0,  0,  0,  9,  0,  0,  0,  0,  0,  7,  0,  0,  0,  0],
    [11,  0,  0,  8,  0,  0,  0,  0,  0, 10,  0,  0,  0,  0,  0,  0],
    [0,  0,  9,  0,  1,  0,  0,  3,  0,  0, 14,  0,  0,  0,  0,  0]
]

