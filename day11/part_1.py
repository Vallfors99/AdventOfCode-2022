# input parsing
import itertools
def create_chunks_by_separator(list_of_lines,sep=''):
    '''
    create chunks from a list of lines by separator
    '''
    chunks = [elem for elem in (list(g) for k,g in itertools.groupby(list_of_lines, key=lambda x: x != sep) if k)]
    return chunks

def perform_operation(item_value, monkey_equation):
    
    if monkey_equation[0] == '*':
        if monkey_equation[1] == 'old':
                new_item_value = item_value*item_value
        else:
            new_item_value = item_value*int(monkey_equation[1])
    
    else: #+
        new_item_value = item_value + int(monkey_equation[1])
    return new_item_value

def play_round(monkeys,items_inspected):
    '''play 1 monkey round'''
    for monkey_id,monkey in monkeys.items():
        for i in range(len(monkey["items"])):
            # increase count for items inspected
            if not monkey_id in items_inspected:
                items_inspected[monkey_id] = 1
            else:
                items_inspected[monkey_id]+=1


            old_item_value = monkey["items"][i]
            # calculate worry level
            worry_level = perform_operation(old_item_value, monkey["equation"])
            worry_level = worry_level//3
            # perform test
            if worry_level%monkey["denominator"] == 0:
                destination = monkey["destination_true"]
            else:
                destination = monkey["destination_false"]
            # throw to destination monkey
            monkeys[destination]['items'].append(worry_level)
        
        # remove all items from monkey
        monkeys[monkey_id]["items"] = []
    
    return monkeys, items_inspected

input_file = 'day11\input.txt'
with open(input_file) as infile:
    lines = [line.strip() for line in infile]

monkey_datas = create_chunks_by_separator(lines,'')
print(monkey_datas[0])

# create monkeys
monkeys = {}
for monkey_data in monkey_datas:
    monkey_id = monkey_data[0].split("Monkey ")[1].strip(':')
    monkey_items = monkey_data[1].split("Starting items: ")[-1]
    monkey_items = [int(elem) for elem in monkey_items.strip(' ').split(',')]
    monkey_equation = monkey_data[2].split('= old ')[-1].split(' ')
    monkey_denominator = int(monkey_data[3].split('by ')[-1])
    monkey_destination_true = monkey_data[4].split('monkey ')[-1]
    monkey_destination_false = monkey_data[5].split('monkey ')[-1]

    monkeys[monkey_id] = {"items": monkey_items, "equation": monkey_equation, "denominator": monkey_denominator,"destination_true": monkey_destination_true, "destination_false":monkey_destination_false}
print("stop")


# play rounds
items_inspected = {}
for round_id in range(20):
    monkeys,items_inspected = play_round(monkeys,items_inspected)
print(items_inspected)
items_inspected = {k: v for k, v in sorted(items_inspected.items(),reverse=True, key=lambda item: item[1])}
ids_sorted = list(items_inspected.keys())
print(items_inspected[ids_sorted[0]]* items_inspected[ids_sorted[1]])