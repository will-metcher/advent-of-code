start = 109165
stop = 576723

def calc_valid_passwords_1():
    valid = []
    for i in range(start, stop):
        if contains_adjacent_digits(str(i)) and is_increasing(str(i)):
            valid.append(i)
    return len(valid)

def calc_valid_passwords_2():
    valid = []
    for i in range(start, stop):
        if contains_discrete_doubles(str(i)) and is_increasing(str(i)):
            valid.append(i)
    return len(valid)


def contains_adjacent_digits(num):
    for i in range(len(num)-1):
        if num[i] == num[i+1]:
            return True
    return False

def contains_discrete_doubles(num):
    for i in range(len(num)-1):
        if num[i] == num[i+1]:
            if i == 0:
                if num[i] != num[i+2]:
                    return True
            elif i == len(num) - 2:
                if num[i] != num[i-1]:
                    return True
            else:
                if num[i] != num[i-1] and num[i] != num[i+2]:
                    return True
    return False
        

def is_increasing(num):
    for i in range(len(num)-1):
        if int(num[i]) > int(num[i+1]):
            return False
    return True

print(calc_valid_passwords_2())
