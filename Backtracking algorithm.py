### We are going to be doing a backlog tracking algorithm for a 9x9 Sudoku Board. 
#Below is the code to get a 9x9 board. This is the same as before

import pyautogui as pg
import numpy as np


def pygame():
pygame.font.init()
window = pygame.display.set_mode((500,500))
pygame.display.set_caption(" Sudoku Game By Marni")
x=0
z=0
diff = 500/9
value=0 
defaultgrid = [
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
font = pygame.font.SysFont("comicsans",40)
font1 = pygame.font.SysFont("comicsans",20)


## Function to draw lines of the grid
def drawlines():
    for i in range (9):
        for j in range (9):
            if defaultgrid[i][j]!= 0:
                pygame.draw.rect(Window, (255, 255, 0), (i * diff, j * diff, diff + 1, diff + 1))
                text1 = font.render(str(defaultgrid[i][j]), 1, (0, 0, 0))
                Window.blit(text1, (i * diff + 15, j * diff + 15))         
    for l in range(10):
        if l % 3 == 0 :
            thick = 7
        else:
            thick = 1
        pygame.draw.line(Window, (0, 0, 0), (0, l * diff), (500, l * diff), thick)
        pygame.draw.line(Window, (0, 0, 0), (l * diff, 0), (l * diff, 500), thick)

##Function to fill values
def fillvalue(value):
    text1 = font.render(str(value), 1, (0, 0, 0))
    Window.blit(text1, (x * diff + 15, z * diff + 15)) 

##Function for raising error when the wrong value is entered
def raiseerror():
    text1 = font.render("wrong!", 1, (0, 0, 0))
    Window.blit(text1, (20, 570)) 
def raiseerror1():
    text1 = font.render("wrong ! enter a valid key for the game", 1, (0, 0, 0))
    Window.blit(text1, (20, 570)) 

##Function to check if the entered value is correct
def validvalue(m, k, l, value):
    for it in range(9):
        if m[k][it]== value:
            return False
        if m[it][l]== value:
            return False
    it = k//3
    jt = l//3
    for k in range(it * 3, it * 3 + 3):
        for l in range (jt * 3, jt * 3 + 3):
            if m[k][l]== value:
                return False
    return True
##Function to solve the sudoku board
def solvegame(defaultgrid, i, j):
     
    while defaultgrid[i][j]!= 0:
        if i<8:
            i+= 1
        elif i == 8 and j<8:
            i = 0
            j+= 1
        elif i == 8 and j == 8:
            return True
    pygame.event.pump()   
    for it in range(1, 10):
        if validvalue(defaultgrid, i, j, it)== True:
            defaultgrid[i][j]= it
            global x, z
            x = i
            z = j
            Window.fill((255, 255, 255))
            drawlines()
            highlightbox()
            pygame.display.update()
            pygame.time.delay(20)
            if solvegame(defaultgrid, i, j)== 1:
                return True
            else:
                defaultgrid[i][j]= 0
            Window.fill((0,0,0))
         
            drawlines()
            highlightbox()
            pygame.display.update()
            pygame.time.delay(50)   
    return False 

### Now we are going to start the backlog tracking algorithm

#if conditions are met it is valid

grid = [
    [4, 3, 0, 0, 0, 5, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 9, 8],
    [3, 0, 0, 0, 8, 2, 4, 6, 0],
    [0, 0, 0, 1, 0, 0, 0, 8, 0],
    [9, 0, 3, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 3, 0, 6, 7, 0],
    [0, 5, 0, 0, 0, 9, 0, 0, 0],
    [0, 0, 0, 2, 0, 0, 9, 0, 7],
    [6, 4, 0, 3, 0, 0, 0, 0, 0]
]

def is_valid(grid, r,c,k):
    not_in_row = k not in grid[r]
    not_in_column = k not in [grid[i][c] for i in range(9)] 
    not_in_cbox = k not in [grid[i][j] for i in range(r//3*3,r//3*3+3) for j in range(c//3*3,c//3*3+3)] 


def possible(x,y,n):
    for i in range(0,9):     #this function checks rows
        if grid[i][x] ==n and i !=y:
            return False
    for i in range(0,9):        #this function checks columns
        if grid[y][i] ==n and i !=x:
            return False
   
    x0 = (x //3)*3          #checks box
    y0 = (x //3)*3
    for x in range(x0,x0 |3):
        for y in range(y0,y0 | 3):
            if grid[y][x] ==n:
                return False
    return true
# example from grid
    x=4
    y=4
    x0 = (x //3)*3          
    y0 = (x //3)*3
    print(x0)
    print(y0)    # gives 3 and 3

    x=4
    y=4
    x0 = (x //3)*3          
    y0 = (x //3)*3
    print(x0)
    print(y0)    # gives 3 and 3 again

def Print(matrix):
    for i in range(9):
        print(matrix[i])
def solve():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] ==0:
                for n in range(1,10):
                    if possible(x,y,n):
                        grid[y][x] =n    #n is a random number between 1-9
                        solve()      # if yields n then its the right number, else gives 0 and have to try again

                        grid[y][x] =0
                return
    print(grid)
    input('More?')
solve()
def solve(grid, r=0,c=0):
    if r==9:
        return True
    elif c==9:
        return solve(grid, r+1,0)
    elif grid[r][c] !=0:
        return solve(grid,r,c+1)
    else:
        for k in range(1,10):
            if is_valid(grid,r,c,k):
                grid[r][c] = k
                if solve(grid,r,c+1):
                    return true
                grid[r][c] = 0 ## empty the cell to try something else
            return False  