# input parsing
input_file = 'day6\input.txt'
with open(input_file) as infile:
    lines = [line.strip() for line in infile]


result = None
message = [c for c in lines[0]]
for i in range(len(message)):
    if len(set(message[i:i+4])) == 4:
        result = i+4
        break
print(result)