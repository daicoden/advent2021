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


def basin_size(m, n, data, searched):
    rows = len(data)
    cols = len(data[0])

    if m == -1:
        return 0
    if m == rows:
        return 0
    if n == -1:
        return 0
    if n == cols:
        return 0

    if data[m][n] == 9:
        return 0

    if searched[m][n]:
        return 0

    searched[m][n] = True

    return 1 + basin_size(m - 1, n, data, searched) \
           + basin_size(m + 1, n, data, searched) \
           + basin_size(m, n - 1, data, searched) \
           + basin_size(m, n + 1, data, searched)


rows = len(data)
cols = len(data[0])

basin_sizes = []
for point in found_low_points:
    searched = []
    for m in range(rows):
        searched.append([False] * cols)
    basin_sizes.append(basin_size(point[0], point[1], data, searched))


basin_sizes = sorted(basin_sizes, reverse=True)
print(basin_sizes[0] * basin_sizes[1] * basin_sizes[2])
