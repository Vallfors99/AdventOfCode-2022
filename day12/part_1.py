import string
import numpy as np


# input parsing
input_file = 'day12\input.txt'
with open(input_file) as infile:
    lines = [line.strip() for line in infile]

letters = list(string.ascii_lowercase)
val_by_letter = {letters[i]:i for i in range(len(letters))}
val_by_letter['S'] = -1
val_by_letter['E'] = 26

grid = {}
lines = [[elem for elem in line] for line in lines]
for row_idx in range(len(lines)):
    for col_idx in range(len(lines[0])):
        grid[(row_idx,col_idx)] = val_by_letter[lines[row_idx][col_idx]]

start_key = [i for i in grid if grid[i]==-1][0]
stop_key = [i for i in grid if grid[i]==26][0]

print(grid)
print(start_key)
print(stop_key)

# generate all possible paths
paths = []
path = []
all_directions = [(1,0),(-1,0),(0,1),(0,-1)]
# figure out where we can go
current_pos = start_key

i = 0
paths = [[start_key]]
complete_paths = []
visited_positions = {}
i = 0
while complete_paths == []:
    # where can i go?
    new_paths = []
    visited_positions_this_round = []
    print(i)
    for path in paths:
        current_pos = path[-1]
        max_climb_height = grid[current_pos] + 1
        possible_moves = [(path[-1][0]+Drow,path[-1][1]+Dcol) for (Drow,Dcol) in all_directions if (path[-1][0]+Drow,path[-1][1]+Dcol) in grid and grid[(path[-1][0]+Drow,path[-1][1]+Dcol)] <= max_climb_height ]
        
        
        if possible_moves == []: # kolla s.a. inte i mål
            continue

        # create combinations
        for new_pos in possible_moves: # going back or to where another path has already been is suboptimal
            if new_pos in visited_positions:
                continue

            elif not grid[new_pos] == 26:
                new_paths.append(path+[new_pos])
                visited_positions_this_round.append(new_pos)

            else: # complete path; save
                complete_paths.append(path+[new_pos])
                #visited_positions_this_round.append(new_pos)

        for pos in visited_positions_this_round:
            visited_positions[pos] = True
    
    paths = new_paths
    i+=1

for coords in complete_paths[0]:
    print(f'{coords} {grid[coords]}')

grid_height = len(lines)
grid_width = len(lines[0])
print_grid = np.full(fill_value='.',shape=[grid_height,grid_width],dtype=str)
for i in range(len(complete_paths[0])-1):
    delta = (complete_paths[0][i+1][0] - complete_paths[0][i][0], complete_paths[0][i+1][1] - complete_paths[0][i][1])
    
    if delta == (1,0):
        s = "v"
    elif delta == (-1,0):
        s = "^"
    elif delta == (0,-1):
        s = "<"
    else:
        s = ">"
    print_grid[complete_paths[0][i]] = s

print(print_grid)