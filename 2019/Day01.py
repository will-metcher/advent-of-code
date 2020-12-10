import math

f = open("input.txt", "r")
masses = f.readlines()
f.close()

def calc_fuel(mass):
    return math.floor(mass / 3) - 2

def sum_fuel():
    total = 0
    for mass in masses:
        total += calc_fuel(int(mass))

    return total

def sum_fuel_2():
    cum_total = 0
    total = 0
    for mass in masses:
        total = int(mass)
        while total > 0:
            total = calc_fuel(total)
            if total > 0:
                cum_total += total
    return cum_total

print(sum_fuel_2())
