# input parsing
input_file = 'day17\input.txt'
with open(input_file) as infile:
    lines = [line.strip() for line in infile]

lines = [line.replace('Valve ','').replace(' has flow rate=',',').split(';') for line in lines]
lines = [[line[0].split(','),line[1].split(',')] for line in lines]
for idx in range(len(lines)):
    lines[idx][1][0] = lines[idx][1][0].split(' ')[5]
    print(lines[idx])