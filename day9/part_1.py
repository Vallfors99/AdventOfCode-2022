import numpy as np
def get_new_tail_position(pos_head,pos_tail):
    Dx,Dy = (pos_head[0]-pos_tail[0],pos_head[1]-pos_tail[1])
    if abs(Dx) <= 1 and abs(Dy) <= 1:
        return pos_tail

    elif abs(Dx) == 0: #vertical
        pos_tail = (pos_tail[0],pos_tail[1]+Dy//abs(Dy))

    elif abs(Dy) == 0: #horizontal
        pos_tail = (pos_tail[0]+Dx//abs(Dx), pos_tail[1])

    else: #diagonal
        pos_tail = (pos_tail[0]+Dx//abs(Dx),pos_tail[1]+Dy//abs(Dy))

    return pos_tail

def get_grid_size(lines):
    dir_vectors = {"U":(0,1),"D":(0,-1),"L":(-1,0),"R":(1,0)}
    old_head_pos = (0,0)
    visited_positions_head = [(0,0)]
    for direction,steps in lines:
        for step in range(int(steps)):
            head_position = (old_head_pos[0]+dir_vectors[direction][0],old_head_pos[1]+dir_vectors[direction][1])
            old_head_pos = head_position
            visited_positions_head.append(head_position)
    
    # find the maximum and minimum x and y values in the list of tuples
    x_values = [x for x,y in visited_positions_head]
    y_values = [y for x,y in visited_positions_head]
    max_x = max(x_values)
    min_x = min(x_values)
    max_y = max(y_values)
    min_y = min(y_values)
    # build a grid of the right size
    grid_size = (max_x-min_x+1,max_y-min_y+1)
    return grid_size


input_file = "input.txt"
with open(input_file) as infile:
    lines = [line.strip().split(' ') for line in infile]

dir_vectors = {"U":(0,1),"D":(0,-1),"L":(-1,0),"R":(1,0)}
current_positions = {"head":(0,0),"tail":(0,0)}
visited_positions_tail = [(0,0)]

grid_shape = get_grid_size(lines)


for direction,steps in lines:
    dir_vector_head = dir_vectors[direction]
    steps = int(steps)
    for n in range(steps):
        old_position_head = current_positions["head"]
        new_position_head = (old_position_head[0]+dir_vector_head[0], old_position_head[1]+dir_vector_head[1])
        current_positions["head"] = new_position_head

        new_position_tail = get_new_tail_position(current_positions["head"],current_positions["tail"])
        visited_positions_tail.append(new_position_tail)
        current_positions["tail"] = new_position_tail

        '''
        grid_for_print = np.empty(grid_shape,dtype=str)
        grid_for_print[current_positions["head"]] = 'H'
        grid_for_print[current_positions["tail"]] = 'T'
        print('')
        print('')
        print(grid_for_print)
        '''

print(len(set(visited_positions_tail)))
