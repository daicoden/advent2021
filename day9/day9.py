def get_data(filename):
    data = []
    with open(filename) as f:
        for line in f.readlines():
            data.append(list(map(lambda depth: int(depth), line.rstrip())))

    return data


def low_point(m, n, data):
    rows = len(data)
    cols = len(data[0])

    top = False
    left = False
    bottom = False
    right = False

    if m == 0:
        top = True
    if m == rows - 1:
        bottom = True
    if n == 0:
        left = True
    if n == cols - 1:
        right = True

    if not top and data[m - 1][n] > data[m][n]:
        top = True

    if not bottom and data[m + 1][n] > data[m][n]:
        bottom = True

    if not left and data[m][n - 1] > data[m][n]:
        left = True

    if not right and data[m][n + 1] > data[m][n]:
        right = True

    return top and left and bottom and right


def find_low_points(data):
    rows = len(data)
    cols = len(data[0])

    low_points = []

    for m in range(rows):
        for n in range(cols):
            if low_point(m, n, data):
                low_points.append([m, n])
    return low_points


data = get_data('input.txt')
found_low_points = find_low_points(data)

sum = 0
for point in found_low_points:
    sum += data[point[0]][point[1]] + 1


print(sum)
