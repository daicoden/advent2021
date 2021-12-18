class Snail:
    def __init__(self, value, parent=None):
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


input = Snail([[[[[4, 3], 4], 4], [7, [[8, 4], 9]]], [1, 1]])


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
        if left_snail.right_snail().left_leaf() == to_explode:
            left_snail.left += to_explode.left
        else:
            left_snail.right_leaf().right += to_explode.left

    right_snail = to_explode.right_snail()

    if right_snail:
        if right_snail.left_snail().right_leaf() == to_explode:
            print('i thought so')
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
    split_side = None
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



print(input)
print(explode(input))
print(input)
print(explode(input))
print(input)
print(split(input))
print(input)
print(split(input))
print(input)
print(explode(input))

print(input)


"""
for num in input.each_snail():
    print(num)
    print(num.left_snail())
    print(num.right_snail().right_leaf())
    print(num.depth())
    print('--')

"""
