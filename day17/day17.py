def get_data(filename):
    with open(filename) as f:
        str = f.readline()
        coordinates = str.split(':')[1]
        x, y = coordinates.split(',')
        start, end = x.split('=')[1].split('..')
        x = range(int(start), int(end) + 1)
        start, end = y.split('=')[1].split('..')
        y = range(int(start), int(end) + 1)

        return [x, y]


data = get_data('input.txt')
print(data)


def step(x, y, vx, vy):
    x += vx
    y += vy

    vy -= 1
    if vx > 0:
        vx -= 1
    elif vx < 0:
        vx += 1

    return [x, y, vx, vy]


def hit(data, x, y):
    return x in data[0] and y in data[1]


def miss(data, x, y):
    return x > data[0][-1] or y < data[1][0]


hit_trajectories = []
initial_velocities = []
for vvx in range(0, 500):
    for vvy in range(-500, 500):
        x = 0
        y = 0
        maxy = 0
        vx = vvx
        vy = vvy
        # print(f'{vx}, {vy}')
        while not miss(data, x, y):
            x, y, vx, vy = step(x, y, vx, vy)
            if y > maxy:
                maxy = y
            if hit(data, x, y):
                hit_trajectories.append(maxy)
                initial_velocities.append([vvx, vvy])
                break


print(max(hit_trajectories))
print(initial_velocities)
print(len(initial_velocities))
