with open('input.txt') as f:
    lines = f.readlines()

depth = 0
horizontal = 0

for line in lines:
    command, amount = line.split(" ")
    amount = int(amount)
    if command == 'forward':
        horizontal += amount
    if command == 'down':
        depth += amount
    if command == 'up':
        depth -= amount

print(depth*horizontal)
