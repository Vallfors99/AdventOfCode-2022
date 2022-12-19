import cProfile

def elementwise_addition(list_1,list_2):
    '''perform elementwise addition on two lists'''
    for i in range(len(list_1)):
        list_2[i] += list_1[i]
    return list_2


def get_cube_neighbors(cube,other_cubes):
    '''get coordinates for neighbors of cube, if neighbor exists in other_cubes'''
    neighbors = []
    neighbor_1 = elementwise_addition(cube,[0,0,1])
    neighbor_2 = elementwise_addition(cube,[0,0,-1])
    neighbor_3 = elementwise_addition(cube,[0,1,0])
    neighbor_4 = elementwise_addition(cube,[0,-1,0])
    neighbor_5 = elementwise_addition(cube,[1,0,0])
    neighbor_6 = elementwise_addition(cube,[-1,0,0])

    for neighbor in [neighbor_1,neighbor_2,neighbor_3,neighbor_4,neighbor_5,neighbor_6]:
        if tuple(neighbor) in other_cubes:
            neighbors.append(tuple(neighbor))
    return neighbors


def count_external_surfaces(external_air_cubes,cubes):
    '''count how many external surfaces the cube structure has'''
    n_external_surfaces = 0
    for cube in cubes:
        n_external_surfaces += len(get_cube_neighbors(cube,external_air_cubes))
    return n_external_surfaces

def get_all_air_cubes_in_cube_space(cubes):
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
    return air_cubes,min_x,max_x,min_y,max_y,min_z,max_z

def find_all_connected_cubes(start_cube,all_cubes):
    '''
    Takes a start_cube and a list containing all_cubes in the cube space.
    Returns a dict of all cubes that are connected to the start_cube
    either directly or indirectly through other cubes in all_cubes
    '''
    neighbors = {start_cube: True}
    new_neighbors_this_iteration = [start_cube]

    while True:
        print(len(new_neighbors_this_iteration))
        new_neighbors_previous_iteration = new_neighbors_this_iteration
        new_neighbors_this_iteration = []

        for neighbor in new_neighbors_previous_iteration:
            new_neighbors_this_neighbor = get_cube_neighbors(neighbor,all_cubes)
            for new_neighbor in new_neighbors_this_neighbor:
                if not new_neighbor in neighbors:
                    new_neighbors_this_iteration.append(new_neighbor)
        
        new_neighbors_this_iteration = set(new_neighbors_this_iteration)
        if len(new_neighbors_this_iteration) == 0:
            break
        else:
            for new_neighbor in new_neighbors_this_iteration:
                neighbors[new_neighbor] = True

    return neighbors

def main():
    # input parsing
    input_file = 'day18\input.txt'
    with open(input_file) as infile:
        cubes = [[int(elem) for elem in line.strip().split(',')] for line in infile]
        cubes = [(c[0],c[1],c[2]) for c in cubes]

    # get all air cubes in the cube space (including a padding of 1)
    air_cubes,min_x,max_x,min_y,max_y,min_z,max_z = get_all_air_cubes_in_cube_space(cubes)

    # define an edge air cube which is known to be outside of the cube structure
    edge__air_cube = (min_x-1,min_y-1,min_z-1)

    # find all connected air cubes to this air cube
    air_cubes = {air_cube: True for air_cube in air_cubes}
    external_air_cubes = find_all_connected_cubes(edge__air_cube,air_cubes)
    
    # count the number of external surfaces
    n_external_surfaces = count_external_surfaces(external_air_cubes,cubes)
    
    print(n_external_surfaces)
cProfile.run('main()',sort='cumtime')