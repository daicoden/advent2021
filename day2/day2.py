with open('input.txt') as f:
    lines = f.readlines()

depth = 0
horizontal = 0
aim = 0

for line in lines:
    command, amount = line.split(" ")
    amount = int(amount)
    if command == 'forward':
        horizontal += amount
        depth += aim*amount
    if command == 'down':
        aim += amount
    if command == 'up':
        aim -= amount

print(depth*horizontal)
