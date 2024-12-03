import numpy as np
import random


def init_grid():
    grid = np.zeros((4, 4))
    return grid


def add_new(grid):

    # get 0 pos
    zero_pos = []
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i, j] == 0:
                zero_pos.append((i, j))

    if not zero_pos:
        return grid

    # 80% a 2, 20% a 4
    prob = np.random.rand()
    new_num = 2 if prob < 0.8 else 4
    pos = random.choice(zero_pos)
    grid[pos] = new_num
    return grid


# def bad_rollin_row(row):
#     for i in range(len(row) - 1):
#         if row[i] != 0:
#             for j in range(i + 1, len(row)):
#                 if row[j] == row[i]:
#                     row[i] += row[j]
#                     row[j] = 0
#                     break
#                 elif row[j] == 0:
#                     continue
#                 else:
#                     break
#     return row


# 2 2 2 2 -> 4 4 0 0
# bugged
def rollin_row(row):
    for i in range(len(row)):
        while row[i] == 0:
            row = row[:i] + row[i + 1 :] + [row[i]]
        if row[i] != 0 and i != 0:
            if row[i - 1] == row[i]:
                row[i - 1] += row[i]
                row[i] = 0
    return row


# print(rollin_row([2,2,2,2]))


def rollin(grid, dir):
    if dir == "d":
        for i in range(grid.shape[1]):
            grid[:, i] = rollin_row(grid[:, i][::-1])[::-1]
    elif dir == "u":
        for i in range(grid.shape[1]):
            grid[:, i] = rollin_row(grid[:, i])
    elif dir == "l":
        for i in range(grid.shape[0]):
            grid[i] = rollin_row(grid[i])
    elif dir == "r":
        for i in range(grid.shape[0]):
            grid[i] = rollin_row(grid[i][::-1])[::-1]

    return grid


def test():
    grid = init_grid()
    print(grid)
    grid = add_new(grid)
    print(grid)
    grid = add_new(grid)
    print(grid)
    grid = rollin(grid, "d")
    print(grid)


test()
