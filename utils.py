def read_file(name, read_type=""):
    f = open("inputs/" + name + ".txt", 'r')
    if read_type == "lines":
        lines = f.readlines()
    else:
        lines = f.read()
    f.close()
    return lines


def manhatten_distance(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)
