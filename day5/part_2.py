input_file = "input.txt"
with open(input_file) as infile:
    lines = [line.strip('\n') for line in infile]

instructions = []

idx_split = lines.index('')
crates_raw = lines[0:idx_split-1]
instructions = lines[idx_split+1:]
crates_raw= [s.replace('    ',' ') for s in crates_raw]
crates_raw = [elem.split(' ') for elem in crates_raw]

n_bins = max([len(row) for row in crates_raw])
crates = [[] for n in range(n_bins)]
for row in crates_raw:
    for j in range(len(row)):
        if row[j] != '':
            crates[j].append(row[j])
            print(crates[j])

for instruction in instructions:
    instruction = instruction.strip('move ')
    instruction = instruction.replace(' from ',',')
    instruction = instruction.replace(' to ',',')
    instruction = instruction.split(',')
    n,fr,to = instruction
    n = int(n)
    fr = int(fr)
    to = int(to)
    to_move = crates[fr-1][:n] # pick up all at once
    crates[fr-1] = crates[fr-1][n:]
    crates[to-1] = to_move + crates[to-1]
print([b[0].strip('[').strip(']') for b in crates])
