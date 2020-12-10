import math, utils

partitions = utils.read_file("day05", "lines")

def find_row(partition):
    row_f = 0
    row_b = 127
    for r in partition:
        if r == "F":
            row_b -= math.ceil((row_b - row_f) / 2)
        else:
            row_f += math.ceil((row_b - row_f) / 2)
    return row_f

def find_col(partition):
    col_l = 0
    col_r = 7
    for c in partition:
        if c == "R":
            col_l += math.ceil((col_r - col_l) / 2)
        else:
            col_r -= math.ceil((col_r - col_l) / 2)
    return col_r

def calc_id(row, col):
    return (8 * row) + col

def highest_id():
    highest = 0
    for partition in partitions:
        row = find_row(partition[0:7])
        col = find_col(partition[7:])
        seat_id = calc_id(row, col)
        if seat_id > highest:
            highest = seat_id
    return highest

def calc_ids():
    ids = []
    for partition in partitions:
        row = find_row(partition[0:7])
        col = find_col(partition[7:])
        ids.append(calc_id(row, col))
    return sorted(ids)

def find_seat():
    ids = calc_ids()
    for i in range(len(ids)-1):
        if  ids[i] + 1 != ids[i+1]:
            return ids[i] + 1
    return 0

print(find_seat())
        
