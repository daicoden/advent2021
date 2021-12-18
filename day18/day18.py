from copy import deepcopy


class Snail:
    def __init__(self, value=None, parent=None, left=None, right=None):
        if value:
            left = value[0]
            right = value[1]
            if type(left) == int:
                self.left = left
            else:
                self.left = Snail(left, self)

            if type(right) == int:
                self.right = right
            else:
                self.right = Snail(right, self)
        else:
            self.left = left
            self.right = right
            self.left.parent = self
            self.right.parent = self
        self.parent = parent

    def __str__(self):
        return f"[{str(self.left)}, {str(self.right)}]"

    def depth(self):
        count = 0
        pointer = self
        while pointer.parent:
            count += 1
            pointer = pointer.parent

        return count

    def set_left(self, value):
        self.left = value

    def set_right(self, value):
        self.right = value

    def read_left(self):
        return self.left

    def read_right(self):
        return self.right

    def each(self):
        if type(self.left) == int:
            yield self.left
        else:
            for left in self.left.each():
                yield left

        if type(self.right) == int:
            yield self.right
        else:
            for right in self.right.each():
                yield right

    def each_snail(self):
        if type(self.left) == int:
            yield self
        else:
            for left in self.left.each_snail():
                yield left

        if type(self.right) == int:
            # Don't yield two value numbers
            if type(self.left) != int:
                yield self
        else:
            for right in self.right.each_snail():
                yield right

    def root(self):
        if self.parent:
            return self.parent.root()
        else:
            return self

    def left_snail(self):
        last_number = None
        for number in self.root().each_snail():
            if number == self:
                return last_number
            last_number = number

    def right_snail(self):
        snails = [f for f in (self.root().each_snail())]

        last_number = None
        for number in reversed(snails):
            if number == self:
                return last_number
            last_number = number

    def right_leaf(self):
        if type(self.right) == int:
            return self
        return self.right.right_leaf()

    def left_leaf(self):
        if type(self.left) == int:
            return self
        return self.left.left_leaf()

    def is_right(self):
        if not self.parent:
            raise Exception('should not be called as root')
        return self.parent.right == self

    def is_left(self):
        if not self.parent:
            raise Exception('should not be called as root')
        return self.parent.left == self

    def is_parent(self, candidate):
        if candidate == self:
            return True

        if not self.parent:
            return False

        return self.parent.is_parent(candidate)

    def magnitude(self):

        if type(self.left) == int:
            left_value = self.left * 3
        else:
            left_value = self.left.magnitude() * 3

        if type(self.right) == int:
            right_value = self.right * 2
        else:
            right_value = self.right.magnitude() * 2

        return left_value + right_value


def explode(root: Snail):
    to_explode = None
    for snail in root.each_snail():
        if snail.depth() == 4:
            to_explode = snail
            break

    if not to_explode:
        return None

    if type(to_explode.left) != int or type(to_explode.right) != int:
        raise Exception(f"Assumpting violation for {to_explode}")

    left_snail = to_explode.left_snail()
    if left_snail:
        if to_explode.is_parent(left_snail):
            left_snail.left += to_explode.left
        else:
            left_snail.right_leaf().right += to_explode.left

    right_snail = to_explode.right_snail()

    if right_snail:
        if to_explode.is_parent(right_snail):
            right_snail.right += to_explode.right
        else:
            right_snail.left_leaf().left += to_explode.right

    if to_explode.parent.right == to_explode:
        to_explode.parent.right = 0

    if to_explode.parent.left == to_explode:
        to_explode.parent.left = 0

    return to_explode

def split(root: Snail):
    to_split = None
    for snail in root.each_snail():
        if type(snail.left) == int and snail.left > 9:
            to_split = snail
            read = to_split.read_left
            write = to_split.set_left
            break

        if type(snail.right) == int and snail.right > 9:
            to_split = snail
            read = to_split.read_right
            write = to_split.set_right
            break

    if not to_split:
        return None

    left = read() // 2
    right = int(read() / 2.0 + 0.5)

    write(Snail([left, right], to_split))
    return to_split


def process(root: Snail):
    workDone = True
    while workDone:
        workDone = False
        if explode(root):
            workDone = True
            continue

        if split(root):
            workDone = True
            continue

    return root


def get_data(filename):
    data = []
    with open(filename) as f:
        for line in f.readlines():
            data.append(Snail(eval(line)))

    return data


input = get_data('input.txt')
#current = input[0]
#for to_add in input[1:]:
#    print(current)
#    print(to_add)
#    current = Snail(left=current, right=to_add)
#    print(current)
#    process(current)
#    print(current)

#print(current.magnitude())

max = 0
for first in input:
    for second in input:
        if first == second:
            continue

        mag = process(Snail(left=deepcopy(first), right=deepcopy(second))).magnitude()
        if mag > max:
            max = mag

print(max)

"""
for num in input.each_snail():
    print(num)
    print(num.left_snail())
    print(num.right_snail().right_leaf())
    print(num.depth())
    print('--')

"""
