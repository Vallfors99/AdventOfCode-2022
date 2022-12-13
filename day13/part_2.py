
def check_order(pair_left,pair_right):
    # get both into lists
    #print(f'{pair_left}, {pair_right}')
    if isinstance(pair_left,int) and isinstance(pair_right,int):
        if pair_left < pair_right:
            #print('Left side is smaller, so inputs are in the right order')
            return True
        elif pair_left == pair_right:
            return None
        else:
            #print('Right side is smaller, so inputs are not in the right order')
            return False
    if not isinstance(pair_left,list):
        pair_left = [pair_left]
    if not isinstance(pair_right,list):
        pair_right = [pair_right]

    for idx in range(len(pair_left)):
        if idx > len(pair_right)-1:
            #print('Right side ran out of items, so inputs are not in the right order')
            return False
        outcome = check_order(pair_left[idx],pair_right[idx])
        if outcome == False:
            return False
        if outcome == True:
            return True

    if len(pair_left) < len(pair_right):
        #print('Left side ran out of items, so inputs are in the right order')
        return True
    else:
        return None

# input parsing
input_file = 'day13\input.txt'
with open(input_file) as infile:
    lines = [line.strip() for line in infile if line != '\n']

# build list of packets
packets = []
for idx in range(len(lines)):
    str_to_execute_1 = f'packets.append({lines[idx]})'
    exec(str_to_execute_1)


# compare to all and get scores, most smaller
total_score = {}
# add divider packets
packets.append([[2]])
packets.append([[6]])

# sort packets
for i in range(len(packets)):
    total_score[i] = 0
    for j in range(len(packets)):
        if j != i:
            if not check_order(packets[i],packets[j]):
                total_score[i]+=1

packet_idx_sorted = list({k: v for k, v in sorted(total_score.items(), key=lambda item: item[1])}.keys())
packets = [packets[idx] for idx in packet_idx_sorted]

# get indices of divider packets
divider_1_idx = packets.index([[2]])+1
divider_2_idx = packets.index([[6]])+1
#print results
print(divider_1_idx*divider_2_idx)