import string


# parse input
input_file = 'day3\input.txt'
with open(input_file) as infile:
    rugsacks = [line.strip('\n') for line in infile]

# generate alphabetical list with associated values
alphabet = list(string.ascii_lowercase) + list(string.ascii_uppercase)
value_by_letter = {alphabet[i]:i+1 for i in range(len(alphabet))}

# split rugsacks into groups of three
n = 3
groups = [rugsacks[i * n:(i + 1) * n] for i in range((len(rugsacks) + n - 1) // n )]

# calculate total priority
total_priority = 0
for sack_1,sack_2,sack_3 in groups:
    # find the letter that is shared by all 3 sacks
    common_letters = set([elem for elem in sack_1 if elem in sack_2 and elem in sack_3])
    total_priority += sum([value_by_letter[letter] for letter in common_letters])
print(total_priority)