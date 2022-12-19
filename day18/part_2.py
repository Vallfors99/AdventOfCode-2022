# input parsing
input_file = 'day18\input.txt'
with open(input_file) as infile:
    cubes = [[int(elem) for elem in line.strip().split(',')] for line in infile]
    cubes = [(c[0],c[1],c[2]) for c in cubes]

area_count = 0

# build cubes for test
cubes = []
for x in range(1,5,1):
    for y in range(1,5,1):
        for z in range(1,5,1):
            if (x,y,z) not in cubes:
                cubes.append((x,y,z))
cubes.remove((1,1,1))
print(cubes)
# make big cube
# iterate over all air cubes
# if air cube can see one or more surfaces but not 6 surfaces, then all of those surfaces are external
# if air cube can see 6 surfaces, then all of those surfaces are internal
# all surfaces should be seen by air cubes

# build big cube
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


# count visible surfaces
visible_surfaces = []
cubes_xy = set([(cube[0],cube[1]) for cube in cubes])
cubes_xz = set([(cube[0],cube[2]) for cube in cubes])
cubes_yz = set([(cube[1],cube[2]) for cube in cubes])

for air_cube in air_cubes:
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
                    visible_surfaces_air_cube['x+'] = (cube,5) 
                elif abs(cube[0]-air_cube[0]) < abs(visible_surfaces_air_cube['x+'][0][0]-air_cube[0]):
                    visible_surfaces_air_cube['x+'] = (cube,5) 
            elif cube[0] < air_cube[0]:
                if visible_surfaces_air_cube['x-'] == None:
                    visible_surfaces_air_cube['x-'] = (cube,6)
                elif abs(cube[0]-air_cube[0]) < abs(visible_surfaces_air_cube['x-'][0][0]-air_cube[0]): 
                    visible_surfaces_air_cube['x-'] = (cube,6)

    visible_surfaces_air_cube = [elem for elem in visible_surfaces_air_cube.values() if elem != None]
    if len(visible_surfaces_air_cube) < 6:
        for elem in visible_surfaces_air_cube:
            visible_surfaces.append(elem)
print(len(set(visible_surfaces)))
