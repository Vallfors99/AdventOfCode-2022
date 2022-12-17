# imports:
from itertools import groupby
import collections

# functions:
def create_chunks_by_separator(list_of_lines,sep=''):
    '''
    create chunks from a list of lines by separator
    '''
    chunks = [elem for elem in (list(g) for k,g in groupby(list_of_lines, key=lambda x: x != sep) if k)]
    return chunks

# input parsing:
input_file = 'day17\input.txt'
with open(input_file) as infile:
    # extract the jet pattern as a list of strings
    jet_stream_queue = collections.deque([[elem for elem in line.strip()] for line in infile][0])

# define rock shapes and store in a deque
shape_1 = [['#','#','#','#']]
shape_2 = [['.','#','.'], ['#','#','#'], ['.','#','.']]
shape_3 = [['.','.','#'], ['.','.','#'], ['#','#','#']]
shape_4 = [['#'],['#'],['#'],['#']]
shape_5 = [['#','#'],['#','#']]
rocks_queue = collections.deque([shape_1,shape_2,shape_3,shape_4,shape_5])

#define initial grid
grid = [['.' for col in range(7)] for row in range(4)]
grid[0] = ['-' for col in range(7)]

for row_idx in reversed(range(len(grid))):
    print("".join(grid[row_idx]))
