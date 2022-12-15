import numpy as np
def get_points_within_manhattan_distance(sensor_pos,manhattan_distance,max_coord):
    print(sensor_pos)
    all_points = []
    
    for x in range(0,max_coord+1):
        for y in range(0,max_coord+1):
            Dx = x-sensor_pos[0]
            Dy = y-sensor_pos[1]
            if abs(Dx)+abs(Dy) <= manhattan_distance:
                all_points.append((x,y))
        

    return all_points
# input parsing
input_file = 'day15\input.txt'

sensor_data = {}
empty_points = []
max_coord = 4000000

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
        # calculate manhattan distance
        sensor_pos = lines[i][0]
        beacon_pos = lines[i][1]
        Dx,Dy = beacon_pos[0]-sensor_pos[0], beacon_pos[1]-sensor_pos[1]
        manhattan_distance = abs(Dx)+abs(Dy)
        # get all points closer than the beacon
        points_closer_than_beacon = get_points_within_manhattan_distance(sensor_pos,manhattan_distance,max_coord)
        for point in points_closer_than_beacon:
            empty_points.append(tuple(point))


empty_points = list(set(empty_points))
beacons = [pos for pos in sensor_data.values()]
sensors = [pos for pos in sensor_data.keys()]
empties= [pos for pos in empty_points]
occupied= set(empties + sensors + beacons)

for x in range(0,max_coord+1):
    for y in range(0,max_coord+1):
        if (x,y) not in occupied:
            print(x,y)