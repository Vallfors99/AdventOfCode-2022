import itertools
import cProfile

def create_chunks_by_separator(list_of_lines,sep=''):
    '''
    create chunks from a list of lines by separator
    '''
    chunks = [elem for elem in (list(g) for k,g in itertools.groupby(list_of_lines, key=lambda x: x != sep) if k)]
    return chunks

def perform_operation(item_value, monkey_equation,monkey_case):
    
    if monkey_case == 1:
            new_item_value = item_value*item_value
    elif monkey_case == 2:
            new_item_value = item_value*monkey_equation[1]
    
    else:
        new_item_value = item_value + monkey_equation[1]
    return new_item_value

def play_round(monkeys,items_inspected,gcd):
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
            worry_level = perform_operation(old_item_value, monkey["equation"],monkey["case"])
            # reduce worry level
            worry_level = worry_level%gcd

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

def main():
    # parse input
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
        
        # create monkey equation and case
        monkey_equation = monkey_data[2].split('= old ')[-1].split(' ')
        if monkey_equation[0] == '*':
            if monkey_equation[1] == 'old':
                monkey_case = 1
            else: # * value
                monkey_case = 2
                monkey_equation[1] = int(monkey_equation[1])
        else: # + value
            monkey_case = 3
            monkey_equation[1] = int(monkey_equation[1])

        monkey_denominator = int(monkey_data[3].split('by ')[-1])
        monkey_destination_true = monkey_data[4].split('monkey ')[-1]
        monkey_destination_false = monkey_data[5].split('monkey ')[-1]
        monkeys[monkey_id] = {"items": monkey_items, "equation": monkey_equation, "denominator": monkey_denominator,"destination_true": monkey_destination_true, "destination_false":monkey_destination_false, "case": monkey_case}

    # get a common denominator
    denominators = [m["denominator"] for m in monkeys.values()]
    gcd = 1
    for val in denominators:
        gcd *= val
    
    # play rounds
    items_inspected = {}
    for round_id in range(10000):
        monkeys,items_inspected = play_round(monkeys,items_inspected,gcd)
        print(f'Round: {round_id+1}')

    # print results
    items_inspected = {k: v for k, v in sorted(items_inspected.items(),reverse=True, key=lambda item: item[1])}
    ids_sorted = list(items_inspected.keys())
    print(items_inspected[ids_sorted[0]]* items_inspected[ids_sorted[1]])
    return None

#cProfile.run('main()')
main()