import utils

program = utils.read_file("day14", "lines")
mem = {}


def apply_mask(mask, n):
    result = ""
    for i in range(len(mask)):
        if mask[i] == "X":
            result += n[i]
        else:
            result += mask[i]
    return bin_to_int(result)


def bin_to_int(b):
    return int(b, 2)


def int_to_36_bit_bin(n):
    binary = bin(n).replace("b", "")
    return ("0" * (36 - len(binary))) + binary


def get_mask(line):
    return line.split(" ")[-1]


def get_address(line):
    return line.split(" ")[0][4:-1]


def get_changed_bits(new, original):
    changes = []
    for c, i, j in new, original:
        if i != j:
            changes.append(c)
    return changes


def run_1():
    mask = get_mask(program[0])
    for i in program:
        if len(i) >= len(mask):
            mask = get_mask(i)
            continue
        address = get_address(i)
        num = apply_mask(mask, int_to_36_bit_bin(int(i.split(" ")[-1])))
        mem[address] = num

    total = 0
    for j in mem.values():
        total += j

    print(total)
    print(mem)


def run_2():
    mask = get_mask(program[0])
    for i in program:
        if len(i) >= len(mask):
            mask = get_mask(i)
            continue
        address = get_address(i)
        result = apply_mask(mask, address)
        changes = get_changed_bits(result, mask)


