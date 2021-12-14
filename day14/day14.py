from collections import Counter


class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next


def get_str(node: Node):
    string = ''
    while node.next:
        string += node.val
        node = node.next

    string += node.val

    return string


def get_data(filename):
    insertion_rules = {}

    with open(filename) as f:
        polymer = f.readline().rstrip()
        last_node = None
        for char in polymer:
            new_node = Node(char, None)
            if last_node:
                last_node.next = new_node
                last_node = new_node
            else:
                first_node = new_node
                last_node = new_node

        # blank line
        f.readline()
        for line in f.readlines():
            insertion = list(map(lambda x: x.strip(), line.rstrip().split('->')))
            insertion_rules[insertion[0]] = insertion[1]

    return [first_node, insertion_rules]


def step(char1, char2, insertion_rules, remaining_iterations):
    combined = char1 + char2
    if remaining_iterations == 0:
        return Counter(combined)

    if combined in insertion_rules:
        return step(char1, insertion_rules[combined], insertion_rules, remaining_iterations - 1) \
               + step(insertion_rules[combined], char2, insertion_rules, remaining_iterations - 1)


polymer, insertion_rules = get_data('test-input.txt')

chars = Counter(get_str(polymer))
most = max(chars, key=chars.get)
min = min(chars, key=chars.get)

print(chars[most] - chars[min])
