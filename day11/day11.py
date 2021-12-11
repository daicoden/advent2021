def get_data(filename):
    data = []
    with open(filename) as f:
        for line in f.readlines():
            data.append(list(map(lambda energy: int(energy), line.rstrip())))

    return data


def increment_adjacent(data, m, n):
    rows = len(data)
    cols = len(data[0])

    if m > 0:
        data[m - 1][n] += 1
    if m < rows - 1:
        data[m + 1][n] += 1
    if n > 0:
        data[m][n - 1] += 1
    if n < cols - 1:
        data[m][n + 1] += 1
    if m > 0 and n > 0:
        data[m - 1][n - 1] += 1
    if m > 0 and n < cols - 1:
        data[m - 1][n + 1] += 1
    if m < rows - 1 and n > 0:
        data[m + 1][n - 1] += 1
    if m < rows - 1 and n < cols - 1:
        data[m + 1][n + 1] += 1


def step(data):
    rows = len(data)
    cols = len(data[0])

    flashed = []
    for m in range(rows):
        flashed.append([False] * cols)

    for m in range(rows):
        for n in range(cols):
            data[m][n] += 1

    found_flash = True
    while found_flash:
        found_flash = False
        for m in range(rows):
            for n in range(cols):
                if data[m][n] > 9 and not flashed[m][n]:
                    increment_adjacent(data, m, n)
                    flashed[m][n] = True
                    found_flash = True

    flashed_count = 0
    for m in range(rows):
        for n in range(cols):
            if data[m][n] > 9:
                flashed_count += 1
                data[m][n] = 0

    return flashed_count


data = get_data('input.txt')

sum = 0
for i in range(100):
    sum += step(data)

def print_data(data):
    rows = len(data)
    cols = len(data[0])
    for m in range(rows):
        for n in range(cols):
            print(data[m][n], end='')
        print('')

print_data(data)
print(sum)
