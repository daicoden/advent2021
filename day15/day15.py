from copy import deepcopy


def get_data(filename):
    data = []
    with open(filename) as f:
        for line in f.readlines():
            data.append(list(map(lambda energy: int(energy), line.rstrip())))

    return data


data = get_data('input.txt')

rows = len(data)
cols = len(data[0])

new_data = []

for m in range(rows * 5):
    new_data.append([])
    for n in range(cols * 5):
        new_data[m].append(0)

for superm in range(5):
    for supern in range(5):
        for m in range(rows):
            for n in range(cols):
                new_data[superm * rows + m][supern * cols + n] = data[m][n] + superm + supern
                if new_data[superm * rows + m][supern * cols + n] > 9:
                    new_data[superm * rows + m][supern * cols + n] -= 9

data = new_data
rows = len(data)
cols = len(data[0])

visited = []

for m in range(rows):
    visited.append([])
    for n in range(cols):
        visited[m].append(False)


def path_total(path):
    return sum(map(lambda c: data[c[0]][c[1]], path))


def search(m, n, path):
    rows = len(data)
    cols = len(data[0])

    if m < 0 or m == rows or n < 0 or n == cols:
        return None

    if [m, n] in path:
        return None

    if visited[m][n]:
        return None

    path[1][0] = m
    path[1][1] = n
    return path


def find_min(paths):
    min_total = 100000
    max_length = 0
    current_selection = None
    for count in range(len(paths)):
        path = paths[count]
        if path[0] < min_total:  # and len(path) > max_length:
            min_total = path[0]
            max_length = len(path)
            current_selection = count

    return current_selection


def bredth_first():
    paths = [[0, [0, 0]]]

    rows = len(data)
    cols = len(data[0])

    count = 0
    while True:
        next_index = find_min(paths)
        count += 1
        if count % 100 == 0:
            print(len(paths))

        copy = deepcopy(paths[next_index])
        del paths[next_index]
        up = [deepcopy(copy), copy[-1][0] + 1, copy[-1][1]]
        right = [deepcopy(copy), copy[-1][0], copy[-1][1] + 1]
        down = [deepcopy(copy), copy[-1][0] - 1, copy[-1][1]]
        left = [deepcopy(copy), copy[-1][0], copy[-1][1] - 1]

        for direction in [up, right, down, left]:
            if search(direction[1], direction[2], direction[0]):
                direction[0][0] += data[direction[1]][direction[2]]

                if direction[1] == rows - 1 and direction[2] == cols - 1:
                    return direction[0]

                paths.append(direction[0])
                visited[direction[1]][direction[2]] = True


print(bredth_first())
