# imports:
from itertools import groupby
import collections

# functions:
def drop_rock(grid,rocks_queue:collections.deque,jet_stream_queue: collections.deque):
    '''drop a single rock into the grid'''
    has_landed = False
    # add empty rows
    idx_current_rocks_height = len(grid)-1
    for i in range(3):
        grid.append(['.','.','.','.','.','.','.'])
    # spawn rock positions
    rock_positions = rocks_queue[0]
    rock_positions = [ [len(grid)-1-coords[0], coords[1]]for coords in rock_positions ]    
    print(rock_positions)
    
    while not has_landed:
        old_rock_positions = rock_positions
        # get jet stream direction
        jet_dir = 1 if [jet_stream_queue[0]]=='>' else -1
        jet_stream_queue.rotate()
        # get new coordinates after jet push
        for i in range(len(rock_positions)):
            rock_positions[i][1] + jet_dir
        # let rock fall



    return grid, current_height

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

# define loop for rocks falling
for iter in range(10):
    grid,current_height = drop_rock(grid,rocks_queue,jet_stream_queue)

# for row_idx in reversed(range(len(grid))):
#     print("".join(grid[row_idx]))
