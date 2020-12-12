import utils

seats = utils.read_file("day11").split("\n")


def apply_rules(z, max_adjacent):
    global seats
    new_grid = []
    changes = 0
    for x in range(len(seats)):
        row = ""
        for y in range(len(seats[x])):
            seat = seats[x][y]
            if seat == ".":
                row += "."
                continue
            adjacent_seats = get_adjacent_seats(x, y, z)
            if seat == "L" and adjacent_seats == 0:
                row += "#"
                changes += 1
            elif seat == "#" and adjacent_seats >= max_adjacent:
                row += "L"
                changes += 1
            else:
                row += seat
        new_grid.append(row)

    seats = new_grid
    return changes


def is_out_of_bounds(x, y, grid):
    return x < 0 or x > len(grid) - 1 or y < 0 or y > len(grid[0]) - 1


def get_adjacent_seats(sx, sy, z_range):
    filled = 0
    for y in range(-1, 2):
        for x in range(-1, 2):
            for z in range(1, z_range):
                x_pos = sx + (x * z)
                y_pos = sy + (y * z)
                if is_out_of_bounds(x_pos, y_pos, seats):
                    break
                if x_pos == sx and y_pos == sy:
                    continue
                if seats[x_pos][y_pos] != ".":
                    if seats[x_pos][y_pos] == "#":
                        filled += 1
                    break

    return filled


def run(z, max_adjacent):
    changes = apply_rules(z, max_adjacent)
    while changes > 0:
        changes = apply_rules(z, max_adjacent)

    print(''.join(seats).count("#"))


run(2,4)
run(len(seats),5)
