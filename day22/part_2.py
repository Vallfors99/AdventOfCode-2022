from itertools import groupby
from string import ascii_uppercase
import copy
def create_chunks_by_separator(list_of_lines,sep=''):
    '''
    create chunks from a list of lines by separator
    '''
    chunks = [elem for elem in (list(g) for k,g in groupby(list_of_lines, key=lambda x: x != sep) if k)]
    return chunks

def change_dir(old_dir,instruction):
    '''update direction'''
    if instruction == 'L':
        new_dir = old_dir - 1
    elif instruction == 'R':
        new_dir = old_dir + 1
    if new_dir > 3:
        new_dir -= 4
    elif new_dir < 0:
        new_dir += 4
    return new_dir

def carry_out_instruction(current_dir,current_pos,grid,instruction,dir_vectors,grid_start_stop):
    '''carry out instruction'''
    if instruction in uppers: # rotate only
        current_dir = change_dir(current_dir,instruction)
        # update grid for print
        dirs_symbols = ['>','v','<','^']
        grid_for_print[current_pos[0]-1][current_pos[1]-1] = dirs_symbols[current_dir]
        return current_dir,current_pos

    n_steps = instruction
    for n in range(n_steps):
        # define potential new position
        new_pos = (current_pos[0] + dir_vectors[current_dir][0],current_pos[1] + dir_vectors[current_dir][1])
        if new_pos not in grid: # wrap around
            if current_dir == 0: # right; start with leftmost position in row
                new_pos = (current_pos[0],grid_start_stop["row"][current_pos[0]]["start"])
            elif current_dir == 2: # left; start with the rightmost position in row
                new_pos = (current_pos[0],grid_start_stop["row"][current_pos[0]]["stop"])
            elif current_dir == 1: # down; start with the top position in column
                new_pos = (grid_start_stop["col"][current_pos[1]]["start"],current_pos[1])
            elif current_dir == 3: # up; start with the bottom position in column
                new_pos = (grid_start_stop["col"][current_pos[1]]["stop"],current_pos[1])
        # move to new position if possible, otherwise break
        if grid[new_pos] == True:
            current_pos = new_pos

            # update grid for print
            dirs_symbols = ['>','v','<','^']
            grid_for_print[current_pos[0]-1][current_pos[1]-1] = dirs_symbols[current_dir]
        else:
            break
    return current_dir,current_pos

# input parsing
input_file = 'day22\input.txt'
with open(input_file) as infile:
    lines = [line.strip('\n') for line in infile]


map, instructions  = create_chunks_by_separator(lines)
uppers = [l for l in ascii_uppercase]

# parse instructions
instruction_list = []
current_elem = ''
for l in instructions[0]:
    if l not in uppers:
        current_elem += l
    else:
        instruction_list.append(int(current_elem))
        current_elem = l
        instruction_list.append(current_elem)
        current_elem = ''
if current_elem != '':
    if current_elem not in uppers:
        instruction_list.append(int(current_elem))
    else:
        instruction_list.append(current_elem)


# build grid
grid = {}
map = [[elem for elem in l] for l in map]
side_length = max([len(line) for line in map])//3

for row_idx,line in enumerate(map):
    for col_idx,val in enumerate(line):
        if val == '.': # True indicates a tile where we can walk
            grid[(row_idx+1,col_idx+1)] = True
        elif val == '#': # False indicates a tile where we cannot walk
            grid[(row_idx+1,col_idx+1)] = False

grid_start_stop = {"row":{},"col":{}}
grid_for_print = copy.deepcopy(map)
for row,col in grid:
    if row in grid_start_stop["row"]:
        if col < grid_start_stop["row"][row]["start"]:
            grid_start_stop["row"][row]["start"] = col
        elif col > grid_start_stop["row"][row]["stop"]:
            grid_start_stop["row"][row]["stop"] = col
    else:
        grid_start_stop["row"][row] = {}
        grid_start_stop["row"][row]["start"] = col
        grid_start_stop["row"][row]["stop"] = col

    if col in grid_start_stop["col"]:
        if row < grid_start_stop["col"][col]["start"]:
            grid_start_stop["col"][col]["start"] = row
        elif row > grid_start_stop["col"][col]["stop"]:
            grid_start_stop["col"][col]["stop"] = row
    else:
        grid_start_stop["col"][col] = {}
        grid_start_stop["col"][col]["start"] = row
        grid_start_stop["col"][col]["stop"] = row

# define intial values for position and direction
current_dir = 0
current_pos = (1,map[0].index('.') + 1)
dirs_symbols = ['>','v','<','^']
grid_for_print[current_pos[0]-1][current_pos[1]-1] = dirs_symbols[current_dir]

#define dir vectors
dir_vectors = {0:(0,1),1:(1,0),2:(0,-1),3:(-1,0)}


# carry out each instruction
for instruction in instruction_list:
    current_dir,current_pos = carry_out_instruction(current_dir,current_pos,grid,instruction,dir_vectors,grid_start_stop)
print(current_pos[0]*1000 + current_pos[1]*4 + current_dir)
# for line in grid_for_print:
#     print("".join(line))