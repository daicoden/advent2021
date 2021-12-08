class Point:
    def __init__(self, m, n):
        self.m = m
        self.n = n

    def __str__(self):
        return f"{self.m},{self.n}"


class Line:
    def __init__(self, description):
        start, end = description.split("->")
        m, n = start.split(",")
        self.start = Point(int(m), int(n))
        m, n = end.split(",")
        self.end = Point(int(m), int(n))

    def is_orthogonal(self):
        return self.start.m == self.end.m or self.start.n == self.end.n

    def __str__(self):
        return f"({self.start}) -> ({self.end})"

    def max_row(self):
        return self.start.m if self.start.m > self.end.m else self.end.m

    def max_column(self):
        return self.start.n if self.start.n > self.end.n else self.end.n

    def __iter__(self):
        m = self.start.m
        n = self.start.n

        while m != self.end.m or n != self.end.n:
            yield Point(m, n)

            if m < self.end.m:
                m += 1
            elif m > self.end.m:
                m -= 1

            if n < self.end.n:
                n += 1
            elif n > self.end.n:
                n -= 1

        yield Point(m, n)


def run():
    with open('input.txt') as f:
        lines = list(map(lambda line: Line(line), f.readlines()))

    # lines = list(filter(lambda l: l.is_orthogonal(), lines))

    rows = max(lines, key=lambda line: line.max_row()).max_row() + 1
    cols = max(lines, key=lambda line: line.max_column()).max_column() + 1

    board = []
    for m in range(rows):
        board.append([])
        for n in range(cols):
            board[m].append(0)

    for line in lines:
        for point in line:
            board[point.m][point.n] += 1

    total = 0
    for m in range(rows):
        for n in range(cols):
            if board[m][n] > 1:
                total += 1

    print(total)


run()
