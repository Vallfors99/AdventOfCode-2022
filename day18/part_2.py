def elementwise_addition(list_1,list_2):
    '''perform elementwise addition on two lists'''
    for i in range(len(list_1)):
        list_2[i] += list_1[i]
    return list_2


def get_air_cube_neighbors(air_cube,air_cubes):
    '''get coordinates for air cube neighbors of an air cube'''
    neighbors = []
    neighbor_1 = elementwise_addition(air_cube,[0,0,1])
    neighbor_2 = elementwise_addition(air_cube,[0,0,-1])
    neighbor_3 = elementwise_addition(air_cube,[0,1,0])
    neighbor_4 = elementwise_addition(air_cube,[0,-1,0])
    neighbor_5 = elementwise_addition(air_cube,[1,0,0])
    neighbor_6 = elementwise_addition(air_cube,[-1,0,0])

    for neighbor in [neighbor_1,neighbor_2,neighbor_3,neighbor_4,neighbor_5,neighbor_6]:
        if tuple(neighbor) in air_cubes:
            neighbors.append(tuple(neighbor))
    return neighbors

# input parsing
input_file = 'day18\input.txt'
with open(input_file) as infile:
    cubes = [[int(elem) for elem in line.strip().split(',')] for line in infile]
    cubes = [(c[0],c[1],c[2]) for c in cubes]

area_count = 0


# build a big air cube that contains all lava cubes
max_x = max([elem[0] for elem in cubes])
min_x = min([elem[0] for elem in cubes])
max_y = max([elem[1] for elem in cubes])
min_y = min([elem[1] for elem in cubes])
max_z = max([elem[2] for elem in cubes])
min_z = min([elem[2] for elem in cubes])
air_cubes = []
for x in range(min_x-1,max_x+2,1):
    for y in range(min_y-1,max_y+2,1):
        for z in range(min_z-1,max_z+2,1):
            if (x,y,z) not in cubes:
                air_cubes.append((x,y,z))


# identify all external air cubes, i.e. air cubes that are connected to the outermost point
edge_cube = (min_x-1,min_y-1,min_z-1)
neighbors = {edge_cube: True}
new_neighbors_this_iteration = [edge_cube]

while True:
    new_neighbors_previous_iteration = new_neighbors_this_iteration
    new_neighbors_this_iteration = []

    for neighbor in new_neighbors_previous_iteration:
        new_neighbors_this_neighbor = get_air_cube_neighbors(neighbor,air_cubes)
        for new_neighbor in new_neighbors_this_neighbor:
            if not new_neighbor in neighbors:
                new_neighbors_this_iteration.append(new_neighbor)
    
    new_neighbors_this_iteration = set(new_neighbors_this_iteration)
    if len(new_neighbors_this_iteration) == 0:
        break
    else:
        for new_neighbor in new_neighbors_this_iteration:
            neighbors[new_neighbor] = True

# count visible surfaces by iterating over each external air cube and checking which cube surfaces it can see
visible_surfaces = []
cubes_xy = set([(cube[0],cube[1]) for cube in cubes])
cubes_xz = set([(cube[0],cube[2]) for cube in cubes])
cubes_yz = set([(cube[1],cube[2]) for cube in cubes])
external_air_cubes = list(neighbors.keys())
for air_cube in external_air_cubes:

    # check all directions
    visible_surfaces_air_cube = {"x+":None,"x-":None,"y+":None,"y-":None,"z+":None,"z-":None} 
    air_cube_xy = (air_cube[0],air_cube[1])
    air_cube_xz = (air_cube[0],air_cube[2])
    air_cube_yz = (air_cube[1],air_cube[2])

    for cube in cubes:
        if (cube[0],cube[1]) == air_cube_xy:
            if cube[2] > air_cube[2]: # above    
                if visible_surfaces_air_cube["z+"] == None:
                    visible_surfaces_air_cube["z+"] = (cube,0)

                elif abs(cube[2]-air_cube[2]) < abs(visible_surfaces_air_cube["z+"][0][2]-air_cube[2]):
                    # if new cube is closer, it is now the cube that the air cube can see
                    visible_surfaces_air_cube["z+"] = (cube,0)

            if cube[2] < air_cube[2]: # below
                if visible_surfaces_air_cube["z-"] == None:
                    visible_surfaces_air_cube["z-"] = (cube,1)

                elif abs(cube[2]-air_cube[2]) < abs(visible_surfaces_air_cube["z-"][0][2]-air_cube[2]):
                    # if new cube is closer, it is now the cube that the air cube can see
                    visible_surfaces_air_cube["z-"] = (cube,1)

        if (cube[0],cube[2]) == air_cube_xz:
            if cube[1] > air_cube[1]:    
                if visible_surfaces_air_cube['y+'] == None:
                    visible_surfaces_air_cube['y+'] = (cube,2)
                elif abs(cube[1]-air_cube[1]) < abs(visible_surfaces_air_cube['y+'][0][1]-air_cube[1]):
                    visible_surfaces_air_cube['y+'] = (cube,2)
            elif cube[1] < air_cube[1]:
                if visible_surfaces_air_cube['y-'] == None:
                    visible_surfaces_air_cube['y-'] = (cube,3)
                elif abs(cube[1]-air_cube[1]) < abs(visible_surfaces_air_cube['y-'][0][1]-air_cube[1]):
                    visible_surfaces_air_cube['y-'] = (cube,3)

        if (cube[1],cube[2]) == air_cube_yz:    
            if cube[0] > air_cube[0]:
                if visible_surfaces_air_cube['x+'] == None:
                    visible_surfaces_air_cube['x+'] = (cube,4) 
                elif abs(cube[0]-air_cube[0]) < abs(visible_surfaces_air_cube['x+'][0][0]-air_cube[0]):
                    visible_surfaces_air_cube['x+'] = (cube,4) 
            elif cube[0] < air_cube[0]:
                if visible_surfaces_air_cube['x-'] == None:
                    visible_surfaces_air_cube['x-'] = (cube,5)
                elif abs(cube[0]-air_cube[0]) < abs(visible_surfaces_air_cube['x-'][0][0]-air_cube[0]): 
                    visible_surfaces_air_cube['x-'] = (cube,5)

    visible_surfaces_air_cube = [elem for elem in visible_surfaces_air_cube.values() if elem != None]
    for elem in visible_surfaces_air_cube:
        visible_surfaces.append(elem)
# print result
print(len(set(visible_surfaces)))
