
observations = []
displays = []



with open('input.txt') as f:
    for line in f.readlines():
        observation, display = line.split('|')
        observations.append(observation)
        displays.append(display)

count = 0

for display in displays:
    for segment in display.split():
        if len(segment) == 7 or len(segment) == 4 or len(segment) == 3 or len(segment) == 2:
            count += 1

"""
  0:      1:      2:      3:      4:
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....

  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg
 """

segments = {
    'abcefg': '0',
    'cf': '1',
    'acdeg': '2',
    'acdfg': '3',
    'bcdf': '4',
    'abdfg': '5',
    'abdefg': '6',
    'acf': '7',
    'abcdefg': '8',
    'abcdfg': '9'
}


def prune(guesses):
    counts = {
        'a': 0,
        'b': 0,
        'c': 0,
        'd': 0,
        'e': 0,
        'f': 0,
        'g': 0,
    }
    for value, guess in guesses.items():
        for key in counts:
            if key in guess:
                counts[key] += 1

    for key, count in counts.items():
        if count == 1:
            for value, guess in guesses.items():
                if key in guess:
                    guess.clear()
                    guess.append(key)


def decode(observation):
    guesses = {
        'a': ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
        'b': ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
        'c': ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
        'd': ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
        'e': ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
        'f': ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
        'g': ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
    }
    two = [two for two in observation if len(two) == 2][0]
    for value, guess in guesses.items():
        if value not in two:
            guess.remove('c') if 'c' in guess else None
            guess.remove('f') if 'f' in guess else None
    guesses[two[0]] = ['c', 'f']
    guesses[two[1]] = ['c', 'f']

    print(guesses)
    seven = [seven for seven in observation if len(seven) == 3][0]
    print("7 " + seven)
    for value, guess in guesses.items():
        if value not in seven:
            guess.remove('a') if 'a' in guess else None
            guess.remove('c') if 'c' in guess else None
            guess.remove('f') if 'f' in guess else None

    print(guesses)
    prune(guesses)

    four = [four for four in observation if len(four) == 4][0]
    print("4 " + four)
    for value, guess in guesses.items():
        if value not in four:
            guess.remove('b') if 'b' in guess else None
            guess.remove('d') if 'd' in guess else None

    print(guesses)

    if len(guesses['f']) != 2:
        raise Exception('assumption failed')
    if len(guesses['g']) != 2:
        raise Exception('assumption failed')

    if guesses['f'] != guesses['g']:
        raise Exception('Assumption failed')

    for guess in guesses['f']:
        guesses['c'].remove(guess)
        guesses['e'].remove(guess)

    codes_for_nine = set()
    for letter in four:
        codes_for_nine.add(letter)
    for letter in seven:
        codes_for_nine.add(letter)

    print(codes_for_nine)

    nine = [nine for nine in observation if len(nine) == 6 and all(code in nine for code in codes_for_nine)][0]
    letters = [code for code in nine]
    for letter in codes_for_nine:
        letters.remove(letter)
    guesses[letters[0]] = ['g']

    print("9 " + nine)
    prune(guesses)
    print(guesses)

    if len(guesses['f']) != 1:
        raise Exception('Assumption failed')

    two = [two for two in observation if len(two) == 5 and guesses['f'][0] not in two]

    print("2 " + str(two))



decode(observations[0].split())
