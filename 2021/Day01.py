import time
from advent_of_code import utils


def sonar_sweep_1():
    lines = utils.read_file("day01").split("\n")
    increases = 0
    for i in range(len(lines) - 1):
        if int(lines[i + 1]) > int(lines[i]):
            increases += 1
    return increases


def sonar_sweep_2():
    lines = utils.read_file("day01").split("\n")
    increases = 0
    for i in range(len(lines) - 3):
        sum1 = int(lines[i]) + int(lines[i + 1]) + int(lines[i + 2])
        sum2 = int(lines[i + 1]) + int(lines[i + 2]) + int(lines[i + 3])

        if sum2 > sum1:
            increases += 1

    return increases


def main():
    start = time.time()
    print(f'{sonar_sweep_2()} in {time.time() - start} seconds')


if __name__ == "__main__":
    main()
