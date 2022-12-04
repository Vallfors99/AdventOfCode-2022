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

def get_points_between(x1y1,x2y2,inclusive=True,excludeDiagonal=False):
    '''
    get all points between two points provided as tuples
    '''
    dx,dy = x1y1[0] - x2y2[0], x1y1[1] - x2y2[1]
    is_diagonal = abs(dx) == abs(dy) and abs(dx) != 0
    sgn_x = -1 if dx < 0 else 1
    sgn_y = -1 if dy < 0 else 1

    if not is_diagonal:
        if dx != 0 and dy == 0:
            points_between = [(x1y1[0]+i,x1y1[1]) for i in range(0,dx+sgn_x,sgn_x)]

        elif dy != 0 and dx == 0:
            points_between = [(x1y1[0],x1y1[1]+i) for i in range(0,dy+sgn_y,sgn_y)]

        else: #same point twice or non-45-degree diagonal
            points_between = [x1y1]
            if x1y1 != x2y2:
                points_between += x2y2

    elif excludeDiagonal == False:
        points_between = [(x1y1[0]+i*sgn_x,x1y1[1]+i*sgn_y) for i in range(abs(dy)+1)]

    else: 
        points_between = []
    
    if not inclusive:
        points_between.remove(x1y1)
        if x2y2 in points_between:
            points_between.remove(x2y2)
    return points_between

print(get_points_between((-1,-2),(3,3)))