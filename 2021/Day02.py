import time
import utils


def dive_1():
    cmds = utils.read_file("day02").split("\n")
    hor = 0
    depth = 0
    for cmd in cmds:
        if "forward" in cmd:
            hor += int(cmd[-1])
        elif "up" in cmd:
            depth -= int(cmd[-1])
        elif "down" in cmd:
            depth += int(cmd[-1])
    return hor * depth


def dive_2():
    cmds = utils.read_file("day02").split("\n")
    hor = 0
    depth = 0
    aim = 0
    for cmd in cmds:
        if "forward" in cmd:
            hor += int(cmd[-1])
            depth += aim * int(cmd[-1])
        elif "up" in cmd:
            aim -= int(cmd[-1])
        elif "down" in cmd:
            aim += int(cmd[-1])
    return hor * depth


def main():
    start = time.time()
    print(f'{dive_2()} in {time.time() - start} seconds')


if __name__ == "__main__":
    main()
