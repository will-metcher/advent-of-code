import time
import utils


def bin_diagnostic_1():
    lines = utils.read_file("day03").split("\n")
    length = len(lines[0])
    freqs = [0] * length
    for i in range(length):
        for line in lines:
            if line[i] == "1":
                freqs[i] += 1
            else:
                freqs[i] -= 1

    gamma_rate = ""
    for digit in freqs:
        if digit > 0:
            gamma_rate += "1"
        elif digit < 0:
            gamma_rate += "0"

    epsilon_rate = int(utils.logical_not(gamma_rate), 2)
    gamma_rate = int(gamma_rate, 2)
    return gamma_rate * epsilon_rate


def bin_diagnostic_2():
    pass


def main():
    start = time.time()
    utils.print_answer(bin_diagnostic_1(), start)


if __name__ == "__main__":
    main()
