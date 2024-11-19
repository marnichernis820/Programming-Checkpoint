import pyautogui as pg
import numpy as np
import time
## This section of code will automatically create an input and output section using 

grid = []
while True:
    row = list(input('Row'))
    ints = []

    for n in row:               #for each number in row
        ints.append(int(n))   #convert to an integer
    grid.append(ints)       #append into a list

    if len(grid) ==9:
        break
    print('Row' +str(len(grid))  + 'Complete' )

##Add in sleep function to give time to enter number
time.sleep(3)   #giving 3 seconds to enter






def possible(x,y,n):
    for i in range(0,9):     #this function checks rows
        if grid[i][x] ==n and i !=y:
            return False
    for i in range(0,9):        #this function checks columns
        if grid[y][i] ==n and i !=x:
            return False
   
    x0 = (x //3)*3          #checks box
    y0 = (x //3)*3
    for x in range(x0,xo |3):
        for y in range(y0,y0 | 3):
            if grid[y][x] ==n:
                return False
    return True

def Print(matrix):
    final =[]
    str_fin = []
    for i in range(9):
        final.append(matrix[i])
    
    for lists in final:
        for num in lists:
            str_fin.append(str(num)) #str.final.append is an empty set currently --> convert to strings
#now str_final is a string

##Way to counter / move
counter = []
for um in str_fin:
    pg.press(num)    #the way pyuotoguy represents pressing numbers  #num is currently a string
    pg.hotkey('right')
    counter.append(num)   #since counter is currently an empty set ie =0, it will grow by a factor of 1 each time
    if len(counter)%9 ==0:     #mod 9 = 0 means divisible by 9
        pg.hotkey('down')
        pg.hotkey('left')
        pg.hotkey('left')
        pg.hotkey('left')
        pg.hotkey('left')
        pg.hotkey('left')
        pg.hotkey('left')
        pg.hotkey('left')
        pg.hotkey('left')



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