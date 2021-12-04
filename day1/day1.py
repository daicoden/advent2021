

with open('input.txt') as f:
    numbers = list(map(lambda value: int(value), f.read().rstrip().split("\n")))
    print(numbers)
    count = 0
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i -1]:
            count += 1

print(count)


with open('input.txt') as f:
    numbers = list(map(lambda value: int(value), f.read().rstrip().split("\n")))
    print(numbers)
    count = 0
    for i in range(0, len(numbers) - 3):
        if numbers[i] + numbers[i+1] + numbers[i+2] < numbers[i + 1] + numbers[i + 2]+ numbers[i+3]:
            count += 1

print(count)
