
observations = []
displays = []



with open('input.txt') as f:
    for line in f.readlines():
        observation, display = line.split('|')
        observations.append(observation)
        displays.append(display)


count = 0

for display in displays:
    for segment in display.split():
        if len(segment) == 7 or len(segment) == 4 or len(segment) == 3 or len(segment) == 2:
            count += 1


print(count)
