# imports:
from itertools import groupby
import collections
import copy
# functions:
def drop_rock(grid,rocks_queue:collections.deque,jet_stream_queue: collections.deque):
    '''drop a single rock into the grid'''
    has_landed = False
    # add empty rows
    
    while grid[-4] != ['.','.','.','.','.','.','.']: 
        grid.append(['.','.','.','.','.','.','.'])
    # spawn rock positions
    rock_positions = rocks_queue[0]
    rock_positions = [ [len(grid)-1-coords[0], coords[1]]for coords in rock_positions ]    
    

    while not has_landed:
        # save old rock positions
        old_rock_positions = copy.deepcopy(rock_positions)

        # get jet stream direction
        jet_dir = 1 if jet_stream_queue[0] =='>' else -1

        # Perform jet push:
        for i in range(len(rock_positions)):
            new_pos = rock_positions[i]
            new_pos[1] += jet_dir
            if new_pos[1] == 7 or new_pos[1] == -1 or grid[new_pos[0]][new_pos[1]] == '#':
                # no jet push, restore old positions and break
                rock_positions = copy.deepcopy(old_rock_positions)
                break
            # update rock positions for the current rock segment
            rock_positions[i] = new_pos
        
        # rotate jet stream queue 
        jet_stream_queue.rotate(-1)
            
        # save old rock positions as positions after jet push
        old_rock_positions = copy.deepcopy(rock_positions)

        # let rock fall
        for i in range(len(rock_positions)):
            new_pos = rock_positions[i]
            new_pos[0] -= 1
            if grid[new_pos[0]][new_pos[1]] == "#" or grid[new_pos[0]][new_pos[1]] == '-':
                # no fall, rock has landed and the fall should be cancelled
                rock_positions = copy.deepcopy(old_rock_positions)
                has_landed = True
                break
            # update rock positions for the current rock segment
            rock_positions[i] = new_pos
        
    # modify grid
    for rock_position in rock_positions:
        grid[rock_position[0]][rock_position[1]] ='#'
    
    # update rocks queue
    rocks_queue.rotate(-1)
    return grid,rocks_queue,jet_stream_queue

# input parsing:
input_file = 'day17\input.txt'
with open(input_file) as infile:
    # extract the jet pattern as a list of strings
    jet_stream_queue = collections.deque([[elem for elem in line.strip()] for line in infile][0])

# define rock shapes and store in a deque
shape_1 = [['.','.','#','#','#','#','.']]
shape_2 = [['.','.','.','#','.','.','.'], ['.','.','#','#','#','.','.'], ['.','.','.','#','.','.','.']]
shape_3 = [['.','.','.','.','#','.','.'], ['.','.','.','.','#','.','.'], ['.','.','#','#','#','.','.']]
shape_4 = [['.','.','#','.','.','.','.'],['.','.','#','.','.','.','.'],['.','.','#','.','.','.','.'],['.','.','#','.','.','.','.']]
shape_5 = [['.','.','#','#','.','.','.'],['.','.','#','#','.','.','.']]

rock_shapes = [shape_1,shape_2,shape_3,shape_4,shape_5]
rock_shapes_coords = []
for rock_shape in rock_shapes:
    coords_rocks = []
    for row_idx in range(len(rock_shape)):
        for col_idx in range(len(rock_shape[row_idx])):
            if rock_shape[row_idx][col_idx] == "#":
                coords_rocks.append([row_idx,col_idx])
    rock_shapes_coords.append(coords_rocks)
rocks_queue = collections.deque(rock_shapes_coords)

#define initial grid
grid = [['-' for col in range(7)]]
for i in range(3):
    grid.append(['.','.','.','.','.','.','.'])

# define loop for rocks falling
for iter in range(10):
    grid,rocks_queue,jet_stream_queue = drop_rock(grid,rocks_queue,jet_stream_queue)
    print('')
    print('')
    for row_idx in reversed(range(len(grid))):
        print("".join(grid[row_idx]))
