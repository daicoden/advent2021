from collections import Counter

class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next

def get_data(filename):
    insertion_rules = {}

    with open(filename) as f:
        polymer = f.readline().rstrip()
        # blank line
        f.readline()
        for line in f.readlines():
            insertion = list(map(lambda x: x.strip(), line.rstrip().split('->')))
            insertion_rules[insertion[0]] = insertion[1]

    return [polymer, insertion_rules]


def step(polymer, insertion_rules):
    indexes_to_add = []
    for i in range(len(polymer) - 1):
        if polymer[i:i+2] in insertion_rules:
            indexes_to_add.append([i+1, insertion_rules[polymer[i:i+2]]])

    offset = 0
    current_index = 0
    new_polymer = ''
    for to_add in indexes_to_add:
        new_polymer += polymer[current_index:(to_add[0])] + to_add[1]
        current_index = to_add[0]

    new_polymer += polymer[current_index:]

    return new_polymer

polymer, insertion_rules = get_data('input.txt')

print(polymer)
for i in range(10):
    polymer = step(polymer, insertion_rules)
    print(i)


chars = Counter(polymer)
most = max(chars, key=chars.get)
min = min(chars, key=chars.get)

print(chars[most] - chars[min])
