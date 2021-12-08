with open('input.txt') as f:
    crabs = list(map(lambda t: int(t), f.readline().split(",")))

min_position = min(crabs)
max_position = max(crabs)

cache = {0: 0}


def booster_cost(distance):
    if distance in cache:
        return cache[distance]

    total = 0
    while distance > 0:
        total += distance
        distance -= 1

    cache[distance] = total
    return cache[distance]


def fuel_cost(position):
    total = 0
    for crab in crabs:
        total += booster_cost(abs(crab - position))
    return total


print(min(map(lambda p: fuel_cost(p), range(min_position, max_position))))
