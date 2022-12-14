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

def get_new_sand_pos(source,rocks_dict,sand_dict):
    '''Figure out where the sand lands when it falls'''

    sand_pos = source
    while True:
        position_below = (sand_pos[0],sand_pos[1]+1)
        position_down_left = (sand_pos[0]-1,sand_pos[1]+1)
        position_down_right = (sand_pos[0]+1,sand_pos[1]+1)

        if not position_below in rocks_dict and not position_below in sand_dict:
            rocks_below = [position for position in list(rocks_dict.keys()) if position[0]==sand_pos[0] and position[1]>sand_pos[1]]
    
            if not rocks_below:
                sand_pos = None
                break
            else:
                sand_pos = position_below

        elif not position_down_left in rocks_dict and not position_down_left in sand_dict:
            sand_pos = position_down_left
        
        elif not position_down_right in rocks_dict and not position_down_right in sand_dict:
            sand_pos = position_down_right

        else:
            break 
    return sand_pos

# input parsing
input_file = 'day14\input.txt'
with open(input_file) as infile:
    lines = [line.strip().split(' -> ') for line in infile]
lines = [[[int(e) for e in elem.split(',')] for elem in line] for line in lines]

# get all rock positions into a dict
rocks_dict = {}
for line in lines:    
    for i in range(len(line)-1):
        rocks = get_points_between(line[i],line[i+1])
        for rock in rocks:
            rocks_dict[(rock[0],rock[1])] = True

# initialize sand parameters
sand_dict = {}
in_void = False
source = (500,0)
while not in_void:
    new_sand_pos = get_new_sand_pos(source,rocks_dict,sand_dict)

    if new_sand_pos:
        sand_dict[new_sand_pos] = True
    else:
        in_void = True
print(len(sand_dict.keys()))