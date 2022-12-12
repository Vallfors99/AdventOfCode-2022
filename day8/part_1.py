import numpy as np
with open("day8\input.txt") as infile:
    lines = [[int(elem) for elem in line.strip()] for line in infile]

grid = np.array(lines)
grid_visible = np.empty(np.shape(grid),dtype=str)
trees_outside = []
border_count = 0
for row in range(len(grid)):
    for col in range(len(grid[0])):
        tree_height = grid[row][col]
        on_border = row == 0 or col == 0 or row == len(grid)-1 or col == len(grid[0])-1 

        if on_border:
            trees_outside.append((row,col))
            grid_visible[row,col] = str(tree_height)
            border_count += 1

        else:
            # check if visible
            left_row = grid[row][0:col][::-1]
            right_row = grid[row][col+1:len(grid[0])]
            up_row = grid[:,col][0:row][::-1]
            down_row = grid[:,col][row+1:len(grid)]

            if tree_height > max(left_row) or tree_height > max(right_row) or tree_height > max(up_row) or tree_height > max(down_row):
                trees_outside.append((row,col))
                grid_visible[row,col] = str(tree_height)
            
print(grid_visible)
print(len(trees_outside))
