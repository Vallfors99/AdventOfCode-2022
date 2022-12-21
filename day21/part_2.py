# input parsing

input_file = 'day21\input.txt'
with open(input_file) as infile:
    lines = [line.strip().replace(':',' = ') for line in infile]

for i in range(len(lines)-1):
    if lines[i].startswith('humn'):
        lines.remove(lines[i])
    elif lines[i].startswith('root'):
        lines[i] = lines[i].replace(' + ', ' == ')

root_line = [line for line in lines if line.startswith('root')][0]
lines.remove(root_line)
variable_names_delete_strings = [] 
for line in lines:
    var_name = line.split(' = ')[0]
    variable_names_delete_strings.append(f'del {var_name}')

for n in range(3876907167490,3876907167500,1):
    humn = n
    done = False
    while not done:
        done = True
        for line in lines:
            try:
                exec(line)
            except:
                done = False

    # after each try, check if root is true, otherwise clear variables and restart
    exec(root_line)
    print(f'root: {plmp} + {rmtt},delta = {plmp - rmtt} n: {n}')
    if root == True:
        print(f'humn: {n}')
        break
    # clear variables
    for line in variable_names_delete_strings:
        exec(line)