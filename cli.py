# test git
import numpy as np
import random
def init_grid():
    grid = np.zeros((4,4))
    return grid
    
def add_new(grid):
    
    # get 0 pos
    zero_pos = []
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i, j] == 0:
                zero_pos.append((i, j))
    
    if not zero_pos: return grid
    
    # 80% a 2, 20% a 4
    prob = np.random.rand()
    new_num = 2 if prob < 0.8 else 4
    pos = random.choice(zero_pos)
    grid[pos] = new_num
    return grid

    
def bad_rollin_row(row):
    for i in range(len(row)-1):
        if row[i] != 0:
            for j in range(i+1, len(row)):
                if row[j] == row[i]:
                    row[i] += row[j]
                    row[j] = 0
                    break
                elif row[j] == 0:
                    continue
                else:
                    break
    return row
                
# 2 2 2 2 -> 4 4 0 0
def rollin_row(row):
    for i in range(1, len(row)):
        if row[i] == 0:
            row = row[:i] + row[i+1:] + row[i]
        else:
            if row[i-1] == row[i]:
                row[i-1] += row[i]
                row[i] = 0
    return row
    
# print(rollin_row([2,2,2,2]))

def rollin(grid, dir):
    if dir == 'd':
    
    elif dir == 'u':
        
    elif dir == 'l':
        for i in range(grid.shape[0]):
            grid[i] = rollin_row(grid[i])
    elif dir == 'r':
        for i in range(grid.shape[0]):
            gird[i] = rollin_row(grid[i][::-1])[::-1]
