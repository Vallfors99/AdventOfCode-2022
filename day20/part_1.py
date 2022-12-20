from collections import deque
# input parsing
input_file = 'day20\input.txt'
with open(input_file) as infile:
    elements_original_order = [int(line.strip()) for line in infile]

element_positions= dict()
for index,element in enumerate(elements_original_order):
    element_positions[(index,element)] = index
    elements_original_order[index] = (index,elements_original_order[index])
max_pos = len(elements_original_order)-1
min_pos = 0

for element_data in elements_original_order:
    new_element_positions = dict()
    shift_value = element_data[1]
    old_position = element_positions[element_data]
    new_position  = (old_position + shift_value) % (max_pos+1)

    if shift_value == 0:
        continue

    # pop element
    for other_element in elements_original_order:
        if other_element == element_data:
            continue
        other_element_pos = element_positions[other_element]
        if other_element_pos < old_position: # all indices below are increased on pop
            new_element_positions[other_element] = (other_element_pos + 1) % (max_pos+1)
    
        if other_element_pos > old_position: # all indices above are decreased on pop
            new_element_positions[other_element] = (other_element_pos - 1) % (max_pos+1)

        else:
            new_element_positions[other_element] = element_positions[other_element]

    # add element
    for other_element in elements_original_order:
        if other_element == element_data:
            continue
        
        other_element_pos = element_positions[other_element]

        if other_element_pos > new_position:
            new_element_positions[other_element] = (new_element_positions[other_element]+1) % (max_pos+1)
        
        elif other_element_pos == new_position:
            if shift_value > 0:
                new_element_positions[other_element] = (new_element_positions[other_element]) % (max_pos+1)
            else:
                new_element_positions[other_element] = (new_element_positions[other_element]+1) % (max_pos+1)

    for e in new_element_positions:
        element_positions[e] = new_element_positions[e]
    element_positions[element_data] = new_position

    elements_sorted = [e[1] for e in {k: v for k, v in sorted(element_positions.items(), key=lambda item: item[1])}.keys()]
    print(elements_sorted)