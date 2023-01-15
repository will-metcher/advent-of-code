import utils


def get_elf_cals():
    lines = utils.read_file("day01").split("\n")
    index = 0
    elves = [0]
    for line in lines:
        if line == "":
            elves.append(0)
            index += 1
            continue
        elves[index] += int(line)
    return sorted(elves, reverse=True)


if __name__ == "__main__":
    elf_cals = get_elf_cals()
    print(elf_cals[0])
    print(elf_cals[0] + elf_cals[1] + elf_cals[2])
