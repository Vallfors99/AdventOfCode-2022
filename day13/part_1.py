from itertools import groupby

def create_chunks_by_separator(list_of_lines,sep=''):
    '''
    create chunks from a list of lines by separator
    '''
    chunks = [elem for elem in (list(g) for k,g in groupby(list_of_lines, key=lambda x: x != sep) if k)]
    return chunks

def check_order(pair_left,pair_right,idx):
    
    print(pair_left,pair_right)
    if idx > len(pair_right)-1 and not idx > len(pair_left)-1:
        return False
    elif idx > len(pair_left)-1:
        return True

    if isinstance(pair_left[idx],list) and isinstance(pair_right[idx],list):
        idx+=1
        if idx > len(pair_right)-1 and not idx > len(pair_left)-1:
            return False
        elif idx > len(pair_left)-1:
            return True
        check_order(pair_left[idx],pair_right[idx],idx)

    elif isinstance(pair_left[idx],list) or isinstance(pair_right[idx],list):
        if isinstance(pair_left[idx],int):
            pair_left[idx] = list(pair_left[idx])
        
        if isinstance(pair_left[idx],int):
            pair_right[idx] = list(pair_right[idx])
        return check_order(pair_left,pair_right,idx)

    else: # two ints
        if pair_left[idx] < pair_right[idx]:
            return True
        elif pair_left[idx] > pair_right[idx]:
            return False
        else:
            idx +=1
            if idx > len(pair_right)-1 and not idx > len(pair_left)-1:
                return False
            elif idx > len(pair_left)-1:
                return True
            return check_order(pair_left,pair_right,idx)


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
    pair_results.append(check_order([pair[0]],[pair[1]],idx=0))
print(sum([i for i in range(len(pair_results)) if pair_results[i]]))