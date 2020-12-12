import utils

instructions = utils.read_file("day08", "lines")


def accumulator():
    accumulator = 0
    visited_indexes = []
    i = 0
    while i not in visited_indexes:
        visited_indexes.append(i)
        line = instructions[i].split(" ")
        command = line[0]
        value = int(line[1])

        if command == "acc":
            accumulator += value
        elif command == "jmp":
            i += value
            continue
        i += 1

    return accumulator


def accumulator_corrupted():
    for j, ins in enumerate(instructions):
        accumulator = 0
        visited_indexes = []

        if "acc" in ins:
            continue
        new_command = ""
        old_command = instructions[j]

        if "nop" in ins:
            new_command = instructions[j].replace("nop", "jmp")
        else:
            new_command = instructions[j].replace("jmp", "nop")

        instructions[j] = new_command
        i = 0
        while i not in visited_indexes:
            if i == len(instructions):
                return accumulator
            if i >= len(instructions):
                instructions[j] = old_command
                break
            visited_indexes.append(i)
            line = instructions[i].split(" ")
            command = line[0]
            value = int(line[1])
            if command == "acc":
                accumulator += value
            elif command == "jmp":
                i += value
                continue
            i += 1

        instructions[j] = old_command

    return -1


print(accumulator_corrupted())
