from collections import deque
# input parsing
input_file = 'day20\input.txt'
with open(input_file) as infile:
    elements_original_order = [int(line.strip()) for line in infile]

element_positions= dict()
for index,element in enumerate(elements_original_order):
    element_positions[(index,element)] = index
    if element == 0: # save key for element with value 0
        key_0 = (index,element)
    elements_original_order[index] = (index,elements_original_order[index])
max_pos = len(elements_original_order)-1
min_pos = 0

for element_data in elements_original_order:
    new_element_positions = dict()
    shift_value = element_data[1]
    if shift_value < 0:
        shift_value -=1
    old_position = element_positions[element_data]
    new_position  = (old_position + shift_value) % (max_pos+1)

    for elem,pos in element_positions.items():
        if old_position < pos:
            if new_position >= pos:
                new_element_positions[elem] = (pos-1) % (max_pos+1)
            elif new_position < pos:
                new_element_positions[elem] = pos
        elif old_position > pos:
            if new_position > pos:
                new_element_positions[elem] = pos
            elif new_position < pos:
                new_element_positions[elem] = (pos+1) % (max_pos+1)
            else:
                new_element_positions[elem] = (pos-1) % (max_pos+1)
        else:
            new_element_positions[elem] = new_position

    for elem,pos in new_element_positions.items():
        element_positions[elem] = pos


elements_sorted = [e[1] for e in {k: v for k, v in sorted(element_positions.items(), key=lambda item: item[1])}.keys()]
idx_0 = element_positions[key_0]
groove_coordinates = [elements_sorted[(idx_0+1000)%(max_pos+1)],elements_sorted[(idx_0+2000)%(max_pos+1)],elements_sorted[(idx_0+3000)%(max_pos+1)]]
print(sum(groove_coordinates))
