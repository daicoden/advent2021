from collections import Counter


def get_data(filename):
    insertion_rules = {}

    with open(filename) as f:
        polymer = f.readline().rstrip()

        # blank line
        f.readline()
        for line in f.readlines():
            insertion = list(map(lambda x: x.strip(), line.rstrip().split('->')))
            insertion_rules[insertion[0]] = insertion[1]

    return [polymer, insertion_rules]


cache = {}

def step(char1, char2, insertion_rules, remaining_iterations):
    combined = char1 + char2

    cache_key = char1 + char2 + str(remaining_iterations)
    if cache_key in cache:
        return cache[cache_key]

    if remaining_iterations == 0:
        return Counter()

    if combined in insertion_rules:
        counter = Counter(insertion_rules[combined])
        final = counter + step(char1, insertion_rules[combined], insertion_rules, remaining_iterations - 1) \
                + step(insertion_rules[combined], char2, insertion_rules, remaining_iterations - 1)
        cache[cache_key] = final
        return final

    return Counter()


polymer, insertion_rules = get_data('input.txt')

chars = []
for char in polymer:
    chars.append(char)

counter = Counter(polymer)
for i in range(len(chars) - 1):
    print(i)
    counter += step(chars[i], chars[i + 1], insertion_rules, 40)

most = max(counter, key=counter.get)
min = min(counter, key=counter.get)

print(counter[most] - counter[min])
