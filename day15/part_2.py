import numpy as np
import matplotlib.pyplot as plt
def get_all_corners(sensor_pos,beacon_pos):
    Dx,Dy = beacon_pos[0]-sensor_pos[0], beacon_pos[1]-sensor_pos[1]
    manhattan_distance = abs(Dx)+abs(Dy)
    corner_left = (sensor_pos[0]-manhattan_distance,sensor_pos[1])
    corner_right = (sensor_pos[0]+manhattan_distance,sensor_pos[1])
    corner_up = (sensor_pos[0],sensor_pos[1]-manhattan_distance)
    corner_down = (sensor_pos[0],sensor_pos[1]+manhattan_distance)
    corner_coordinates =[corner_left,corner_down,corner_right,corner_up,corner_left]
    # dont forget other stuff that could cause problems
    return corner_coordinates

# input parsing
input_file = 'day15\input.txt'

sensor_data = {}
candidate_points = []
max_coord = 20

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
        sensor_corners = get_all_corners(sensor_pos,beacon_pos)
        print(sensor_corners)

# we know that either, we are in a corner and it is enough to have only one border close to us
# or, if we are not in a corner, there needs to be an intersection or two outer borders
x = [e[0] for e in sensor_corners]
y = [e[1] for e in sensor_corners]
plt.plot(x,y)
plt.show()