import numpy as np
grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print(np.matrix(grid))
def possible(row,column, number): ##is the number appearing in the row, column or box
    global grid
    for i in range(0,9):    #check if number appears in the given row
        if grid[row][i] == number:
            return False
    for i in range(0,9):    #check if number appears in the given column
        if grid[i][column] == number:
            return False

    x0 = (column //3) *3   #check if number apears in box
    y0 = (row //3) *3
    for i in range(0,3):
        for j in range(0,3):
            if grid[y0+i][x0+j] == number:
                return False