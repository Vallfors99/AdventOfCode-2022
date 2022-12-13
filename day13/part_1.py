from itertools import groupby

def create_chunks_by_separator(list_of_lines,sep=''):
    '''
    create chunks from a list of lines by separator
    '''
    chunks = [elem for elem in (list(g) for k,g in groupby(list_of_lines, key=lambda x: x != sep) if k)]
    return chunks

def check_order(pair_left,pair_right):
    # get both into lists
    print(f'{pair_left}, {pair_right}')
    if isinstance(pair_left,int) and isinstance(pair_right,int):
        if pair_left < pair_right:
            print('Left side is smaller, so inputs are in the right order')
            return True
        elif pair_left == pair_right:
            return None
        else:
            print('Right side is smaller, so inputs are not in the right order')
            return False
    if not isinstance(pair_left,list):
        pair_left = [pair_left]
    if not isinstance(pair_right,list):
        pair_right = [pair_right]

    for idx in range(len(pair_left)):
        if idx > len(pair_right)-1:
            print('Right side ran out of items, so inputs are not in the right order')
            return False
        outcome = check_order(pair_left[idx],pair_right[idx])
        if outcome == False:
            return False
        if outcome == True:
            return True

    if len(pair_left) < len(pair_right):
        print('Left side ran out of items, so inputs are in the right order')
        return True
    else:
        return None



# input parsing
input_file = 'day13\input.txt'
with open(input_file) as infile:
    lines = [line.strip() for line in infile]

# split input into pairs
pairs = create_chunks_by_separator(lines,'')

# build pairs using the exec command
pairs_dict = {}
for idx in range(len(pairs)):
    str_to_execute_1 = f'pairs_dict[idx] = [[],[]]'
    str_to_execute_2 = f'pairs_dict[idx][0] = {pairs[idx][0]}'
    str_to_execute_3 = f'pairs_dict[idx][1] = {pairs[idx][1]}'

    exec(str_to_execute_1)
    exec(str_to_execute_2)
    exec(str_to_execute_3)


pair_results = []
for pair in pairs_dict.values():
    pair_results.append(check_order(pair[0],pair[1]))
print(pair_results)
print(sum([idx+1 for idx in range(len(pair_results)) if pair_results[idx]]))