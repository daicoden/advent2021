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


lines = get_lines('test-input.txt')

gamma_lines = lines
epsilon_lines = lines

def keep_matching(gamma_lines, gamma_keep):
    to_keep = []


gamma, foo = extract_gama_epsilon(gamma_lines)
foo, epsilon = extract_gama_epsilon(epsilon_lines)


print(int(gamma, 2) * int(epsilon, 2))
