# group lines into chunks / sublists
from itertools import groupby

def create_chunks_by_separator(list_of_lines,sep=''):
    '''
    create chunks from a list of lines by separator
    '''
    chunks = [elem for elem in (list(g) for k,g in groupby(list_of_lines, key=lambda x: x != sep) if k)]
    return chunks

def create_chunks_by_count(list_of_lines,n:int):
    '''
    create chunks from a list of lines based on the number lines in each chunk
    '''
    chunks = [list_of_lines[i * n:(i + 1) * n] for i in range((len(list_of_lines) + n - 1) // n )]
    return chunks

def get_points_between(x1y1,x2y2,inclusive=True):
    '''Get all points between two points that are in the same row and/or in the same column'''
    dx,dy = x2y2[0] - x1y1[0], x2y2[1] - x1y1[1]
    points_between = [x1y1]
    step_size_x = 0 if dx == 0 else dx//abs(dx)
    step_size_y = 0 if dy == 0 else dy//abs(dy)
    if min(abs(dx),abs(dy)) > 0:
        raise ValueError('input positions must be either horizontally or vertically aligned, or in the same position')
    i = 1
    while not x2y2 in points_between:
        points_between.append([x1y1[0]+step_size_x*i,x1y1[1]+step_size_y*i])
        i+=1
    if not inclusive:
        points_between.remove(x1y1)
        points_between.remove(x2y2)
    return points_between