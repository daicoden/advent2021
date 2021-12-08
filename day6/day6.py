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
        print(f"simulated day {i}. Now have {len(fishes)}, growth = {len(fishes)/fish_count}")


run(80)

print(len(fishes))
