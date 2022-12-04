# input parsing
input_file = 'day4\input.txt'
with open(input_file) as infile:
    lines = [line.strip() for line in infile]

include_count = 0
for line in lines:
    range_1,range_2 =line.split(',')
    range_1 = [int(elem) for elem in range_1.split('-')]
    range_2 = [int(elem) for elem in range_2.split('-')]
    range_1 = [elem for elem in range(range_1[0],range_1[1]+1)]
    range_2 = [elem for elem in range(range_2[0],range_2[1]+1)]
    if (min(range_1) in range_2 and max(range_1) in range_2) or (min(range_2) in range_1 and max(range_2) in range_1):
        include_count += 1
        print(include_count)