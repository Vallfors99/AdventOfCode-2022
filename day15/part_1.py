import numpy as np
def get_points_within_manhattan_distance(sensor_pos,manhattan_distance):
    all_points = []
    for Dx in range(-manhattan_distance,manhattan_distance+1,1):
        for Dy in range(-manhattan_distance,manhattan_distance+1,1):
            if abs(Dx)+abs(Dy) <= manhattan_distance:
                all_points.append((sensor_pos[0]+Dx,sensor_pos[1]+Dy))


    return all_points
# input parsing
input_file = 'day15\input.txt'

sensor_data = {}
empty_points = []

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
        points_closer_than_beacon = get_points_within_manhattan_distance(sensor_pos,manhattan_distance)
        for point in points_closer_than_beacon:
            empty_points.append(tuple(point))


empty_points = list(set(empty_points))
for y in [2000000]:
    beacons_in_row = [pos for pos in sensor_data.values() if pos[1] == y]
    sensors_in_row = [pos for pos in sensor_data.keys() if pos[1] == y]
    empties_in_row = [pos for pos in empty_points if pos[1]==y]
    occupied_in_row = set(empties_in_row + sensors_in_row)
    beacons_in_row = set(beacons_in_row)
    occupied_in_row = occupied_in_row - beacons_in_row
    print(f'y = {y}, occupied = {len(occupied_in_row)}')
