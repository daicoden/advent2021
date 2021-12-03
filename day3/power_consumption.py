def get_lines(file_name):
    with open(file_name) as f:
        text = f.read().rstrip()
        return text.split('\n')


lines = get_lines('star-1.txt')
middle = len(lines)/2
print(len(lines))
print(middle)

histogram = [0] * len(lines[0])

for line in lines:
    i = 0
    for char in line:
        histogram[i] += int(char)
        i += 1
        

gamma = ''
epsilon = ''

print(histogram)
print(middle)


for position in histogram:
    if position > middle:
        gamma += '1'
        epsilon += '0'
    elif position < middle:
        gamma += '0'
        epsilon += '1'
    else:
        raise Exception("Can't handle same value for gama position")


print(int(gamma,2) * int(epsilon, 2))
