import numpy as np
import matplotlib.pyplot as plt

def findIntersection(x1,y1,x2,y2,x3,y3,x4,y4):
    px=( (x1*y2-y1*x2)*(x3-x4)-(x1-x2)*(x3*y4-y3*x4) ) / ( (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4) ) 
    py=( (x1*y2-y1*x2)*(y3-y4)-(y1-y2)*(x3*y4-y3*x4) ) / ( (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4) )
    return [px, py]

def get_perimeter_outside_border(sensor_pos,beacon_pos):
    Dx,Dy = beacon_pos[0]-sensor_pos[0], beacon_pos[1]-sensor_pos[1]
    manhattan_distance = abs(Dx)+abs(Dy)
    corner_left = (sensor_pos[0]-manhattan_distance-1,sensor_pos[1])
    corner_right = (sensor_pos[0]+manhattan_distance+1,sensor_pos[1])
    corner_up = (sensor_pos[0],sensor_pos[1]-manhattan_distance-1)
    corner_down = (sensor_pos[0],sensor_pos[1]+manhattan_distance+1)
    corner_coordinates =[corner_left,corner_down,corner_right,corner_up,corner_left]
    border_lines_down = [[corner_left[0],corner_left[1],corner_down[0],corner_down[1]],[corner_up[0],corner_up[1],corner_right[0],corner_right[1]]]
    border_lines_up = [[corner_down[0],corner_down[1],corner_right[0],corner_right[1]],[corner_left[0],corner_left[1],corner_up[0],corner_up[1]]]
    return corner_coordinates, border_lines_down,border_lines_up

# input parsing
input_file = 'day15\input.txt'

sensor_data = {}
candidate_points = []
max_coord = 4000000
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
lines_down_all = []
lines_up_all = []
with open(input_file) as infile:
    lines = [line.strip().split(':') for line in infile]
    for i in range(len(lines)):
        # parse input data
        lines[i][0] = lines[i][0].strip('Sensor at ').replace('=','').replace('x','').replace('y','').replace(' ','').split(',')
        lines[i][1] = lines[i][1].strip(' closest beacon is at ').replace('=','').replace('x','').replace('y','').replace(' ','').split(',')
        lines[i][0] = [int(elem) for elem in lines[i][0]]
        lines[i][1] = [int(elem) for elem in lines[i][1]]

        # store closest beacon in sensor data
        sensor_data[tuple(lines[i][0])] = tuple(lines[i][1])
        sensor_pos = lines[i][0]
        beacon_pos = lines[i][1]

        # get data for the perimeter outside of the sensors border
        perimeter_corners,lines_down,lines_up = get_perimeter_outside_border(sensor_pos,beacon_pos)
        for l in lines_down:
            lines_down_all.append(l)
        for l in lines_up:
            lines_up_all.append(l)
        
        # plot current perimeter
        x = [e[0] for e in perimeter_corners]
        y = [e[1] for e in perimeter_corners]
        plt.plot(x,y)


# plot desired region
plt.axis([0,max_coord,0,max_coord])
plt.grid(visible=True)
#plt.show()

# initialize list of valid candidates. Corners must be checked.
valid_candidates = [(0,max_coord),(0,0),(max_coord,0),(max_coord,max_coord)]

# get all line intersections. The valid candidates are either corners or intersections of the perimeter of the border
for i in range(len(lines_down_all)):
    for j in range(len(lines_up_all)):
        x1,y1,x2,y2 = lines_down_all[i]
        x3,y3,x4,y4 = lines_up_all[j]
        x_res,y_res = findIntersection(x1,y1,x2,y2,x3,y3,x4,y4)

        # store line intersection if within boundaries
        if x_res >= 0 and x_res <= max_coord and y_res >= 0 and y_res <= max_coord and x_res.is_integer() and y_res.is_integer():
            valid_candidates.append((int(x_res),int(y_res)))
valid_candidates = list(set(valid_candidates))

# get all beacon positions
beacon_coords = set(list(sensor_data.values()))

# check each intersection
print(len(valid_candidates))
for candidate in valid_candidates:
    is_valid = True
    for sensor_pos,beacon_pos in sensor_data.items():
        Dx_beacon,Dy_beacon = beacon_pos[0]-sensor_pos[0], beacon_pos[1]-sensor_pos[1]
        manhattan_beacon = abs(Dx_beacon)+abs(Dy_beacon)
        
        Dx_candidate,Dy_candidate = candidate[0]-sensor_pos[0], candidate[1]-sensor_pos[1]
        manhattan_candidate = abs(Dx_candidate) + abs(Dy_candidate)
        if not manhattan_candidate > manhattan_beacon:
            is_valid = False
            break
    
    # if the candidate is valid, print results
    if is_valid and not candidate in beacon_coords:
        print(candidate)
        print(candidate[0]*4000000+candidate[1])
