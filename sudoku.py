import numpy as np

# Add sudoku here , put zeros in the unknown spots 

grid  = [[5,3,0,0,7,0,0,0,0],
         [6,0,0,1,9,5,0,0,0],
         [0,9,8,0,0,0,0,6,0],
         [8,0,0,0,6,0,0,0,3],
         [4,0,0,8,0,3,0,0,1],
         [7,0,0,0,2,0,0,0,6],
         [0,6,0,0,0,0,2,8,0],
         [0,0,0,4,1,9,0,0,5],
         [0,0,0,0,8,0,0,7,9]]

print ("Input Grid")
print (np.matrix(grid))

# Finds the possibility of number "n" fitting in spot ["y","x"] 

def possibility(y,x,n):
    global grid
    # Check for same number in row
    for i in range (0,9):   
        if grid[y][i] == n:
            return False 
    # Check for same number in coloumn
    for i in range (0,9):   
        if grid[i][x] == n:
            return False 
    # Check for same number in box
    x0 = (x//3)*3 # This floor divion round-offs division to the nearest interger 
    y0 = (y//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if grid[y0+i][x0+j] == n:
                return False 
    return True 

def solve():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1,10):
                    if possibility(y,x,n):
                        grid[y][x] = n
                        solve()
                        grid[y][x] = 0
                return
    print ("Solved Grid ?")
    print (np.matrix(grid))
    input("Keras mas solutiones ?")

solve()
print ("No mas :( ")
