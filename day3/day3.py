import string


# parse input
input_file = 'day3\input.txt'
with open(input_file) as infile:
    rugsacks = [line.strip('\n') for line in infile]
    # split rugsacks by the middle into two compartments
    rugsacks_with_compartments = [(line[:len(line)//2],line[len(line)//2:]) for line in rugsacks]

# generate alphabetical list with associated values
alphabet = list(string.ascii_lowercase) + list(string.ascii_uppercase)
value_by_letter = {alphabet[i]:i+1 for i in range(len(alphabet))}

# calculate the total priority
total_priority = 0
for compartment_1,compartment_2 in rugsacks_with_compartments:
    non_unique_letters = set([elem for elem in compartment_1 if elem in compartment_2])
    total_priority += sum([value_by_letter[letter] for letter in non_unique_letters])
print(total_priority)