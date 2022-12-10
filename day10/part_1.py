input_file = "input.txt"
with open(input_file) as infile:
    lines = [line.strip() for line in infile]
lines = [l.split(' ') for l in lines]
register_val = [1]
for command_val in lines:
    if len(command_val) ==1 and command_val[0] == "noop": #1 cycle, no change in register val
        register_val.append(register_val[-1])

    else: # two cycles
        command,val = command_val
        val = int(val)
        register_val.append(register_val[-1])
        register_val.append(register_val[-1]+val)

signal_strengths = [(i+1)*register_val[i] for i in range(19,249,40)]
print(sum(signal_strengths))
