import string
import numpy as np


# input parsing
input_file = 'day12\input.txt'
with open(input_file) as infile:
    lines = [line.strip() for line in infile]

letters = list(string.ascii_lowercase)
val_by_letter = {letters[i]:i for i in range(len(letters))}
val_by_letter['S'] = 0
val_by_letter['E'] = 26

grid = {}
lines = [[elem for elem in line] for line in lines]
for row_idx in range(len(lines)):
    for col_idx in range(len(lines[0])):
        grid[(row_idx,col_idx)] = val_by_letter[lines[row_idx][col_idx]]

start_keys = [i for i in grid if grid[i]==0]
stop_key = [i for i in grid if grid[i]==26][0]
grid[stop_key] = 25

# generate all possible paths
paths = []
path = []
all_directions = [(1,0),(-1,0),(0,1),(0,-1)]
complete_paths_all = []
for idx,start_key in enumerate(start_keys):
    paths = [[start_key]]
    complete_paths = []
    visited_positions = {}
    i = 0
    print(f'Start key {idx}/{len(start_keys)}')
    while paths != [] and complete_paths == []:
        # where can i go?
        new_paths = []
        visited_positions_this_round = []
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

                elif not new_pos == stop_key:
                    new_paths.append(path+[new_pos])
                    visited_positions_this_round.append(new_pos)

                else: # complete path; save
                    complete_paths.append(path+[new_pos])
                    complete_paths_all.append(len(path+[new_pos]))
                    visited_positions_this_round.append(new_pos)

            for pos in visited_positions_this_round:
                visited_positions[pos] = True
        
        paths = new_paths
        i+=1

complete_paths_all.sort()
print(complete_paths_all)