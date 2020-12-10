import utils

adapters = sorted(list(map(int, utils.read_file("day10", "lines"))))
adapters.insert(0, 0)
adapters.append(adapters[-1] + 3)


def find_differences():
    differences = {"1": 0, "3": 0}
    for i in range(len(adapters) - 1):
        diff = adapters[i + 1] - adapters[i]
        if diff <= 3:
            differences[str(diff)] += 1
        else:
            break
    print(differences["1"] * differences["3"])


def find_distinct_arrangements():
    # number of paths to each index
    paths = [0] * (adapters[-1] + 1)
    paths[0] = 1

    for i in range(1, adapters[-1] + 1):
        # check if i - 1, - 2, etc in adapters, increment path
        for j in range(1, 4):
            if i - j in adapters:
                paths[i] += paths[i - j]

    return paths[-1]


print(find_distinct_arrangements())
