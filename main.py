#!/usr/bin/python3
# main.py
from Board import Grid
grid = Grid.Grid()
print("Py2048 in the terminal. Commands are h(left) j(down) k(up) l(right)") 
while (True):
    print(grid)
    old_grid = Grid.Grid()
    for i in list(range(len(grid.grid))):
        for j in list(range(len(grid.grid[i]))):
            old_grid.grid[i][j] = grid.grid[i][j]
    command = input("Enter command: ")
    if (command == 'h'):
        grid.shift_x(-1)
    elif (command == 'l'):
        grid.shift_x(1)
    elif (command == 'j'):
        grid.shift_y(-1)
    elif (command == 'k'):
        grid.shift_y(1)
    else:
        print("Invalid Input. Try again")
    if (grid == old_grid):
        print("Move not made.")
    else:
        grid.update_unoccupied_ids()
        grid.insert_new_randoms()
