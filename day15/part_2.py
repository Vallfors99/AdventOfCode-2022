import numpy as np
import matplotlib.pyplot as plt

def findIntersection(x1,y1,x2,y2,x3,y3,x4,y4):
    px=( (x1*y2-y1*x2)*(x3-x4)-(x1-x2)*(x3*y4-y3*x4) ) / ( (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4) ) 
    py=( (x1*y2-y1*x2)*(y3-y4)-(y1-y2)*(x3*y4-y3*x4) ) / ( (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4) )
    return [px, py]

def get_all_corners(sensor_pos,beacon_pos):
    Dx,Dy = beacon_pos[0]-sensor_pos[0], beacon_pos[1]-sensor_pos[1]
    manhattan_distance = abs(Dx)+abs(Dy)
    corner_left = (sensor_pos[0]-manhattan_distance-1,sensor_pos[1])
    corner_right = (sensor_pos[0]+manhattan_distance+1,sensor_pos[1])
    corner_up = (sensor_pos[0],sensor_pos[1]-manhattan_distance-1)
    corner_down = (sensor_pos[0],sensor_pos[1]+manhattan_distance+1)
    corner_coordinates =[corner_left,corner_down,corner_right,corner_up,corner_left]
    # dont forget other stuff that could cause problems

    # lines:
    border_lines_UL = [[corner_left[0],corner_left[1],corner_down[0],corner_down[1]],[corner_up[0],corner_up[1],corner_right[0],corner_right[1]]]
    border_lines_UR = [[corner_down[0],corner_down[1],corner_right[0],corner_right[1]],[corner_left[0],corner_left[1],corner_up[0],corner_up[1]]]
    return corner_coordinates, border_lines_UL,border_lines_UR

# input parsing
input_file = 'day15\input.txt'

sensor_data = {}
candidate_points = []
max_coord = 4000000
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
lines_UL_all = []
lines_UR_all = []
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
        # get all extended lines
        sensor_corners,lines_UL,lines_UR = get_all_corners(sensor_pos,beacon_pos)
        for l in lines_UL:
            lines_UL_all.append(l)
        for l in lines_UR:
            lines_UR_all.append(l)
        x = [e[0] for e in sensor_corners]
        y = [e[1] for e in sensor_corners]
        plt.plot(x,y)
# we know that either, we are in a corner and it is enough to have only one border close to us
# or, if we are not in a corner, there needs to be an intersection or two outer borders


# plot good region
plt.axis([0,max_coord,0,max_coord])
plt.grid(visible=True)
#plt.show()

c = 0
valid_candidates = []
# check all line intersections - ignoring the fact that lines are actually segmented
for i in range(len(lines_UL_all)):
    for j in range(len(lines_UR_all)):
        x1,y1,x2,y2 = lines_UL_all[i]
        x3,y3,x4,y4 = lines_UR_all[j]
        x_res,y_res = findIntersection(x1,y1,x2,y2,x3,y3,x4,y4)
        if x_res >= 0 and x_res <= max_coord and y_res >= 0 and y_res <= max_coord and x_res.is_integer() and y_res.is_integer():
            valid_candidates.append((int(x_res),int(y_res)))
        c += 1
valid_candidates = list(set(valid_candidates))
valid_candidates.sort()

# get all beacon positions
beacon_coords = set(list(sensor_data.values()))
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

    if is_valid and not candidate in beacon_coords:
        print(candidate)
        print(candidate[0]*4000000+candidate[1])
# dont forget corners
