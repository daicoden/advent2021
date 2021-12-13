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

first_fold = deepcopy(data)
print(to_folds)
fold(to_folds[0][0], to_folds[0][1], first_fold)

print(list(map(lambda o: str(o), first_fold)))
my_list = list(set(first_fold))

if to_folds[0][0] > 0:
    rows = rows // 2
else:
    cols = cols // 2

print(list(map(lambda o: str(o), my_list)))
print(len(my_list))
