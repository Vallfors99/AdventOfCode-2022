# input parsing
input_file = 'day21\input.txt'
with open(input_file) as infile:
    lines = [line.strip().replace(':',' = ') for line in infile]


done = False
while not done:
    done = True
    for line in lines:
        try:
            exec(line)
        except:
            done = False

print(root)