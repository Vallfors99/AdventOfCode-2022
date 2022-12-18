# input parsing
input_file = 'day18\input.txt'
with open(input_file) as infile:
    cubes = [[int(elem) for elem in line.strip().split(',')] for line in infile]
print(cubes)

area_count = 0
for cube in cubes:
    cube_up = [cube[0],cube[1],cube[2]+1]
    cube_down = [cube[0],cube[1],cube[2]-1]
    cube_x_right = [cube[0]+1,cube[1],cube[2]]
    cube_x_left = [cube[0]-1,cube[1],cube[2]]
    cube_y_right = [cube[0],cube[1]+1,cube[2]]
    cube_y_left = [cube[0],cube[1]-1,cube[2]]
    adjacent_cubes = [cube_up,cube_down,cube_x_left,cube_x_right,cube_y_left,cube_y_right]

    for adj_cube in adjacent_cubes:
        if adj_cube not in cubes:
            area_count += 1
print(area_count)