# imports:
from itertools import groupby
import collections
import copy
# functions:
def print_grid(grid):
    print(" ")
    for row_idx in reversed(range(len(grid))):
                        print("".join(grid[row_idx]))
    print(" ")

def drop_rock(grid,rocks_queue:collections.deque,jet_stream_queue: collections.deque,jet_rotation):
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
            if new_pos[1] == 7 or new_pos[1] == -1 or (new_pos[0] < len(grid) and grid[new_pos[0]][new_pos[1]] == '#'):
                # no jet push, restore old positions and break
                rock_positions = copy.deepcopy(old_rock_positions)
                break
            # update rock positions for the current rock segment
            rock_positions[i] = new_pos
        
        # rotate jet stream queue 
        jet_stream_queue.rotate(-1)
        jet_rotation+=1
        # save old rock positions as positions after jet push
        old_rock_positions = copy.deepcopy(rock_positions)

        # let rock fall
        for i in range(len(rock_positions)):
            new_pos = rock_positions[i]
            new_pos[0] -= 1
            if (new_pos[0] < len(grid) and grid[new_pos[0]][new_pos[1]] == '-') or (new_pos[0] < len(grid) and grid[new_pos[0]][new_pos[1]] == "#"):
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
    return grid,rocks_queue,jet_stream_queue,jet_rotation

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

rock_shapes = [shape_1,shape_2,shape_3[::-1],shape_4,shape_5]

rock_shapes_coords = []
for rock_shape in rock_shapes:
    coords_rocks = []
    for row_idx in range(len(rock_shape)):
        for col_idx in range(len(rock_shape[row_idx])):
            if rock_shape[row_idx][col_idx] == "#":
                coords_rocks.append([-row_idx,col_idx])
    rock_shapes_coords.append(coords_rocks)
rocks_queue = collections.deque(rock_shapes_coords)

#define initial grid
grid = [['-' for col in range(7)]]
for i in range(3):
    grid.append(['.','.','.','.','.','.','.'])

# define loop for rocks falling
start_rocks = copy.deepcopy(rocks_queue)
start_jets_2 = copy.deepcopy(jet_stream_queue.rotate(-2))
stack_heights = []
stack_heights_old = {}
delta_old = {}
iters_old = {}
extra_stack_height = 0
jet_rotation = 0
max_iters = 1000000000000
iter = 0
have_skipped = False
while iter < max_iters:

    # check if any repeats
    if not have_skipped:
        for n in [4]:
            has_printed_blank = False
            if (jet_rotation+n)%len(jet_stream_queue) == 0:
                #print_grid(grid)
                if not has_printed_blank:
                    print(' ')
                    has_printed_blank = True
                if n not in stack_heights_old:
                    stack_heights_old[n] = 0
                if not n in iters_old:
                    iters_old[n] = iter
                if not n in delta_old:
                    delta_old[n] = 0

                stack_height = 0
                for row in grid:
                    if '#' in row:
                        stack_height +=1
                
                print(f'stack height: {stack_height}')
                print(f'n: {n} | {stack_height-stack_heights_old[n]}, {iter-iters_old[n]},{rocks_queue[0]}')
                delta_new = stack_height-stack_heights_old[n] 
                if delta_new == delta_old[n] and delta_new > 0: # safe to start block skipping
                    delta_iters = iter - iters_old[n]
                    n_skips = (max_iters-iter)//delta_iters
                    iter = iter+n_skips*delta_iters
                    extra_stack_height += n_skips*delta_new
                    print(f'skipping: new iter = {iter}, extra stack height = {extra_stack_height}')
                    have_skipped = True
                    print_grid(grid)
                else:
                    iters_old[n] = iter
                    delta_old[n] = delta_new
                    stack_heights_old[n] = stack_height
                    iter+=1
                    print(iter)
            else:
                iter +=1
                print(iter)
    else:
        iter+=1
        print(iter)
    grid,rocks_queue,jet_stream_queue,jet_rotation = drop_rock(grid,rocks_queue,jet_stream_queue,jet_rotation)

stack_height = 0
for row in grid:
    if '#' in row:
        stack_height +=1

print(extra_stack_height+stack_height)
