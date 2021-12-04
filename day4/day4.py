class Board:
    def __init__(self, data):
        self.board = data
        self.solved = []
        self.rows = len(data)
        self.cols = len(data[0])

        for m in range(0, self.rows):
            self.solved.append([])
            for n in range(0, self.cols):
                self.solved[m].append(False)

    def mark_number(self, number):
        for m in range(0, self.rows):
            for n in range(0, self.cols):
                if self.board[m][n] == number:
                    self.solved[m][n] = True

    def is_solved(self):
        for m in range(0, self.rows):
            if False not in self.solved[m]:
                return True

        for n in range(0, self.cols):
            row_match = True
            for m in range(0, self.rows):
                if not self.solved[m][n]:
                    row_match = False

            if row_match:
                return True

        return False

    def unmarked_score(self):
        sum = 0
        for m in range(0, self.rows):
            for n in range(0, self.cols):
                if not self.solved[m][n]:
                    sum += self.board[m][n]

        return sum

    def print(self):
        for m in range(0, self.rows):
            for n in range(0, self.cols):
                print(self.board[m][n], end='')
                print(" ", end='')
            print("")

        print("")
        for m in range(0, self.rows):
            for n in range(0, self.cols):
                print('1' if self.solved[m][n] else '0', end='')
                print(" ", end='')
            print("")


def create_board(lines):
    board = []
    for line in lines:
        board.append(list(map(lambda value: int(value),  line.split())))

    return Board(board)


with open('star-1.txt') as f:
    lines = f.read().split("\n")
    numbers_to_draw = list(map(lambda value: int(value), lines[0].split(",")))
    boards = []
    board_lines = []
    for line in lines[2:]:
        if not line:
            boards.append(create_board(board_lines))
            board_lines = []
        else:
            board_lines.append(line)

solved = None

current_index = -1
while not solved:
    current_index += 1
    for board in boards:
        board.mark_number(numbers_to_draw[current_index])

    solved = next((board for board in boards if board.is_solved()), None)



solved.print()
print(current_index)
print(solved.unmarked_score())
print(numbers_to_draw[current_index])
print(solved.unmarked_score() * numbers_to_draw[current_index])
