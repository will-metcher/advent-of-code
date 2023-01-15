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
    lines = utils.load_input('day03')
    valid_lines = lines.copy()

    i = 0
    while len(valid_lines) > 1:
        freq = 0
        for line in valid_lines:
            if line[i] == "1":
                freq += 1
            else:
                freq -= 1

        if freq >= 0:
            valid_lines = [line for line in valid_lines if line[i] == '1']
        else:
            valid_lines = [line for line in valid_lines if line[i] == '0']

        i += 1
        if i == len(lines[0]):
            break

    oxygen_rating = ''.join(valid_lines)

    valid_lines = lines.copy()

    i = 0
    while len(valid_lines) > 1:
        freq = 0
        for line in valid_lines:
            if line[i] == "1":
                freq += 1
            else:
                freq -= 1

        if freq >= 0:
            valid_lines = [line for line in valid_lines if line[i] == '0']
        else:
            valid_lines = [line for line in valid_lines if line[i] == '1']

        i += 1
        if i == len(lines[0]):
            break

    co2_rating = ''.join(valid_lines)



    return int(oxygen_rating, 2) * int(co2_rating, 2)


def main():
    start = time.time()
    utils.print_answer(bin_diagnostic_2(), start)


if __name__ == "__main__":
    main()
