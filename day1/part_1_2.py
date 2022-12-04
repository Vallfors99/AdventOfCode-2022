# input parsing
input_file = 'day1\input.txt'
with open(input_file) as infile:
    lines = [line.strip('\n') for line in infile]

# part 1
calories_by_elf = {}
elf_id = 0
calory_sum = 0
for line in lines:
    if line == '':
        elf_id +=1
        calories_by_elf[elf_id] = calory_sum
        calory_sum = 0
    else:
        calory_sum += int(line)
if calory_sum !=0:
    elf_id +=1
    calories_by_elf[elf_id] = calory_sum
print(max(calories_by_elf.values()))

#part 2
inventory_totals = list(calories_by_elf.values())
inventory_totals.sort(reverse=True)
print(sum(inventory_totals[0:3]))