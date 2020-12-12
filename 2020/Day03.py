import utils

lines = utils.read_file("day03", "lines")


def slopes(dx, dy):
    x = 0
    trees = 0
    for i in range(0, len(lines), dy):
        if lines[i][x % 31] == "#":
            trees += 1
        x += dx
    return trees


print(slopes(1, 1) * slopes(3, 1) * slopes(5, 1) * slopes(7, 1) * slopes(1, 2))
