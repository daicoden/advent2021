def get_data(filename):
    with open(filename) as f:
        str = '{0:b}'.format(int(f.readline(), 16))
        padding = 0
        return ''.join(['0'] * padding + [str])


def parse_instruction(data, instructions=[], index=0):
    version = int(data[index:index + 3], 2)
    index += 3
    type = int(data[index:index + 3], 2)
    index += 3

    bitcount = 6

    # Literal
    if type == 4:
        byte = '10000'
        constructed = ''
        while byte[0] != '0':
            byte = data[index:index + 5]
            index += 5
            bitcount += 5
            constructed += byte[1:]

        # index += bitcount % 4

        instructions.append([version, type, int(constructed, 2)])
        return index
    else:
        mode = data[index]
        index += 1
        if mode == '0':
            subpacket_length = int(data[index:index+15], 2)
            index += 15
            subpacket_index = index
            instructions.append([version, type, mode, subpacket_length])

            while subpacket_index - index < subpacket_length:
                subpacket_index = parse_instruction(data, instructions, subpacket_index)

            if subpacket_index - index != subpacket_length:
                print(f'something went wrong, parsed {subpacket_index - index} bits instead of {subpacket_length}')
                raise Exception('Fail')

            return subpacket_index
        elif mode == '1':
            subpacket_count = int(data[index:index+11], 2)
            index += 11
            instructions.append([version, type, mode, subpacket_count])

            for i in range(subpacket_count):
                index = parse_instruction(data, instructions, index)

            return index

        else:
            raise Exception(f"Can't handle operator {mode}")

data = get_data('input.txt')
print(data)

instructions = []
parse_instruction(data, instructions)

print(instructions)

count = 0
for instruction in instructions:
    count += instruction[0]

print(count)
