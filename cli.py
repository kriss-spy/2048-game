import numpy as np
import random


def init_grid():
    grid = np.zeros((4, 4), dtype=int)
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


# 2 2 2 2 -> 4 4 0 0
# 0 2 2 0 -> 4 0 0 0
# 0 0 2 2 -> 4 0 0 0
# 0 2 0 2 -> 4 0 0 0
# 1. if 0 between, move
# 2. if equals, combine
# 3. loop until end (no 0 between and no two same numbers)


def rollin_row(row):
    l = len(row)
    flag = True
    while flag:
        flag = False
        for i in range(l - 1):
            if row[i] == 0 and row[i + 1] != 0:
                row[i], row[i + 1] = row[i + 1], row[i]
                flag = True
        for i in range(l - 1):
            if row[i] != 0 and row[i] == row[i + 1]:
                row[i] += row[i + 1]
                row[i + 1] = 0
                flag = True

    return row


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
    # grid = init_grid()
    # print("init:\n", grid)
    grid = np.array([[8, 0, 0, 0], [0, 0, 0, 0], [2, 4, 0, 0], [0, 0, 0, 0]])

    grid = rollin(grid, "d")
    print("after rollin:")
    print("grid:\n", grid)


# test()

import os
import platform


def clear_console():
    # Check the current operating system
    if platform.system() == "Windows":
        os.system("cls")  # Clear console for Windows
    else:
        os.system("clear")  # Clear console for macOS and Linux


def my2048():
    grid = init_grid()
    gird = add_new(grid)
    print(grid)
    while True:
        dir = input("> ")
        if dir == "q":
            break
        if dir not in "lrud":
            clear_console()
            print(f"Unknow command {dir}")
            print("Press l, r, u, or d + Enter")
            print(grid)
            continue
        origin_grid = np.copy(grid)
        grid = rollin(grid, dir)
        if np.array_equal(grid, origin_grid):
            clear_console()
            if not np.any(grid == 0):
                print(grid)
                print("Game Over ! :(")
                break
            print("The grid is stuck")
            print("Move in another direction")
            print(grid)
            continue
        grid = add_new(grid)
        clear_console()
        print(grid)
        # for i in grid:
        #     for j in i:
        #         print(j, end=" ")
        #     print()


if __name__ == "__main__":
    my2048()
