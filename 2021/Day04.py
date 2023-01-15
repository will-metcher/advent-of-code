import time
import utils


def bingo_1():
    with open("inputs/day04.txt") as f:
        lines = [i.strip() for i in f.readlines()]

    calls = lines.pop(0).split(",")

    boards = []
    rows = []
    for line in lines:
        if line == "" and len(rows) > 0:
            boards.append(rows)
            rows = []
        rows.append(line.split(" "))

    return boards[0][1]


def bingo_2():
    pass


def main():
    start = time.time()
    utils.print_answer(bingo_1(), start)


if __name__ == "__main__":
    main()
