def get_data(filename):
    with open(filename) as f:
        data = list(map(lambda line: line.rstrip(), f.readlines()))
    return data


data = get_data("input.txt")

open_values = ['(', '[', '{', '<']
close_values = [')', ']', '}', '>']


def validate(line, stack, index=0):
    #  If we're incemplete
    if len(line) == index and len(stack) != 0:
        return stack

    if len(line) == index:
        return None

    if line[index] in open_values:
        stack.append(line[index])
        return validate(line, stack, index + 1)

    token_index = close_values.index(line[index])
    if open_values[token_index] == stack[-1]:
        stack.pop()
        return validate(line, stack, index + 1)

    return line[index]


errored_data = []

SCORES = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

CLOSED_SCORES = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4,
}

scores = []
for line in data:
    result = validate(line, [], 0)
    if isinstance(result, list):
        score = 0
        for missing in reversed(result):
            score *= 5
            score += CLOSED_SCORES[missing]

        scores.append(score)


print(sorted(scores)[len(scores)//2])
