with open('input.txt') as f:
    fishes = list(map(lambda t: int(t), f.readline().split(",")))


def simulate_day():
    existing_fishes = len(fishes)
    for i in range(existing_fishes):
        fishes[i] -= 1
        if fishes[i] < 0:
            fishes[i] = 6
            fishes.append(8)


def run(days):
    for i in range(days):
        fish_count = len(fishes)
        simulate_day()
        # print(f"simulated day {i}. Now have {len(fishes)}, growth = {len(fishes) / fish_count}")


cache = {}


def simulate(spawn_time, days_left):
    count = 0
    if days_left < 0:
        return 0
    days_left = days_left - spawn_time
    if days_left in cache:
        return cache[days_left]

    total_children = -(days_left // -7)
    count += total_children
    for new_fish in range(total_children):
        count += simulate(0, days_left - 2 - (7 * (new_fish + 1)))
    cache[days_left] = count
    return count


total_count = 0
for fish in fishes:
    total_count += 1 + simulate(fish, 256)

print(total_count)
