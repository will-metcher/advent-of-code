import utils

database = utils.read_file("day02", "lines")

def valid_passwords_1():
    total = 0
    for line in database:
        line = line.split(" ")
        rnge = line[0].split("-")
        lower = int(rnge[0])
        upper = int(rnge[1])
        char = line[1].replace(":","")
        password = line[2]
        occurences = calc_char_occurences(char, password)
        if(occurences >= lower and occurences <= upper):
            total += 1
    return total

def valid_passwords_2():
    total = 0
    for line in database:
        line = line.split(" ")
        rnge = line[0].split("-")
        i1 = int(rnge[0])
        i2 = int(rnge[1])
        char = line[1].replace(":","")
        password = line[2]
        if(bool(password[i1-1] == char) ^ bool(password[i2-1] == char)):
            total += 1
    return total
        

def calc_char_occurences(char, string):
    total = 0
    for c in string:
        if c == char:
            total += 1
    return total

print(valid_passwords_2())
