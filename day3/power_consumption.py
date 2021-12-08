def get_lines(file_name):
    with open(file_name) as f:
        text = f.read().rstrip()
        return text.split('\n')


def extract_gama_epsilon(lines):
    middle = len(lines) / 2

    histogram = [0] * len(lines[0])

    for line in lines:
        i = 0
        for char in line:
            histogram[i] += int(char)
            i += 1

    gamma = ''
    epsilon = ''

    for position in histogram:
        if position > middle:
            gamma += '1'
            epsilon += '0'
        elif position < middle:
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '1'

    return [gamma, epsilon]


def ogygen_rating(lines, index):
    if len(lines) == 1:
        return lines[0]

    ones = 0
    zeros = 0
    for line in lines:
        if line[index] == '0':
            zeros += 1
        if line[index] == '1':
            ones += 1

    if ones >= zeros:
        lines = list(filter(lambda line: line[index] == '1', lines))
    else:
        lines = list(filter(lambda line: line[index] == '0', lines))

    return ogygen_rating(lines, index + 1)

def co2_rating(lines, index):
    if len(lines) == 1:
        return lines[0]

    ones = 0
    zeros = 0
    for line in lines:
        if line[index] == '0':
            zeros += 1
        if line[index] == '1':
            ones += 1

    if ones < zeros:
        lines = list(filter(lambda line: line[index] == '1', lines))
    else:
        lines = list(filter(lambda line: line[index] == '0', lines))

    return co2_rating(lines, index + 1)


oxygen = int(ogygen_rating(get_lines('star-1.txt'), 0), 2)
print(oxygen)
co2 = int(co2_rating(get_lines('star-1.txt'), 0), 2)
print(co2)

print(oxygen * co2)
