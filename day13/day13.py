from copy import deepcopy


class Point:
    def __init__(self, x, y):
        self.n = x
        self.m = y

    def __str__(self):
        return f'{self.n, self.m}'

    def __eq__(self, other):
        return self.n == other.n and self.m == other.m

    def __hash__(self):
        return hash(self.n) + hash(self.m)


def get_data(filename):
    data = []
    folds = []
    append_points = True

    with open(filename) as f:
        for line in f.readlines():
            if not line.rstrip():
                append_points = False
                continue
            if append_points:
                line = line.rstrip()
                data.append(Point(int(line.split(',')[0]), int(line.split(',')[1])))
            else:
                folds.append(line.rstrip())
    return [data, folds]


data, folds = get_data('input.txt')

rows = max(data, key=lambda point: point.m).m
cols = max(data, key=lambda point: point.n).n


def fold(m, n, points):
    if m > 0:
        for point in points:
            if point.m > m:
                point.m = m - (point.m - m)

    if n > 0:
        for point in points:
            if point.n > n:
                point.n = n - (point.n - n)


to_folds = []
for f in folds:
    side, number = f.split("=")
    number = int(number)
    if 'y' in side:
        to_folds.append([number, 0])
    else:
        to_folds.append([0, number])

for f in to_folds:
    fold(f[0], f[1], data)
    if f[0] > 0:
        rows = rows // 2
    else:
        cols = cols // 2

for m in range(rows):
    for n in range(cols):
        if Point(n, m) in data:
            print("X", end='')
        else:
            print('.', end='')
    print('')
