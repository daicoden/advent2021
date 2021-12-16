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
            subpacket_length = int(data[index:index + 15], 2)
            index += 15
            subpacket_index = index
            instructions.append([version, type, mode, None])
            to_update = len(instructions) - 1

            packet_count = 0

            while subpacket_index - index < subpacket_length:
                subpacket_index = parse_instruction(data, instructions, subpacket_index)
                packet_count += 1

            if subpacket_index - index != subpacket_length:
                print(f'something went wrong, parsed {subpacket_index - index} bits instead of {subpacket_length}')
                raise Exception('Fail')

            instructions[to_update][3] = packet_count

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


def run_machine(instructions, index=0):
    instruction = instructions[index]

    if instruction[1] == 0:
        sum = 0
        index += 1
        for i in range(instruction[3]):
            index, result = run_machine(instructions, index)
            sum += result

        return [index, sum]

    if instruction[1] == 1:
        mult = 1
        index += 1
        for i in range(instruction[3]):
            index, result = run_machine(instructions, index)
            mult *= result
        return [index, mult]

    if instruction[1] == 2:
        results = []
        index += 1
        for i in range(instruction[3]):
            index, result = run_machine(instructions, index)
            results.append(result)
        return [index, min(results)]

    if instruction[1] == 3:
        results = []
        index += 1
        for i in range(instruction[3]):
            index, result = run_machine(instructions, index)
            results.append(result)
        return [index, max(results)]

    if instruction[1] == 4:
        return [index + 1, instruction[2]]

    # greater than
    if instruction[1] == 5:
        index += 1
        if instruction[3] != 2:
            raise Exception("should only have 2 arguments")
        index, first_value = run_machine(instructions, index)
        index, second_value = run_machine(instructions, index)
        return [index, 1 if first_value > second_value else 0]

    # less than
    if instruction[1] == 6:
        index += 1
        if instruction[3] != 2:
            raise Exception("should only have 2 arguments")
        index, first_value = run_machine(instructions, index)
        index, second_value = run_machine(instructions, index)
        return [index, 1 if first_value < second_value else 0]

    # eual to
    if instruction[1] == 7:
        index += 1
        if instruction[3] != 2:
            raise Exception("should only have 2 arguments")
        index, first_value = run_machine(instructions, index)
        index, second_value = run_machine(instructions, index)
        return [index, 1 if first_value == second_value else 0]


data = get_data('input.txt')
print(data)

instructions = []
parse_instruction(data, instructions)

print(instructions)

print(run_machine(instructions))
