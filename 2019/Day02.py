import utils

opcodes = utils.read_file("day02").split(",")

ints = list(map(int, opcodes))
print(ints)

def intcode(lst, noun, verb):
    lst[1] = noun
    lst[2] = verb
    for i in range(0, len(lst), 4):
        if lst[i] == 99:
            break
        elif lst[i] == 1:
            lst[lst[i + 3]] = lst[lst[i + 1]] + lst[lst[i + 2]]
        elif lst[i] == 2:
            lst[lst[i + 3]] = lst[lst[i + 1]] * lst[lst[i + 2]]
    return lst[0]


def find_noun_and_verb():
    for noun in range(100):
        for verb in range(100):
            if intcode(ints.copy(), noun, verb) == 19690720:
                return 100 * noun + verb
    return -1


print(find_noun_and_verb())
