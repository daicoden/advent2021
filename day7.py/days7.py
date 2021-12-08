with open('input.txt') as f:
    crabs = list(map(lambda t: int(t), f.readline().split(",")))

min_position = min(crabs)
max_position = max(crabs)


def fuel_cost(position):
    total = 0
    for crab in crabs:
        total += abs(crab - position)
    return total


print(min(map(lambda p: fuel_cost(p), range(min_position, max_position))))
