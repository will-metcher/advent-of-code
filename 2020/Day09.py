import utils

length = 25

nums = list(map(int, utils.read_file("day09").split("\n")))


def is_sum_in_list(num, lst):
    for i,n1 in enumerate(lst):
        for j, n2 in enumerate(lst):
            if i == j:
                continue
            if n1 + n2 == num:
                return True
    return False
        

def find_first_weakness():
    for i in range(length, len(nums)):
        if not is_sum_in_list(nums[i], nums[i-length:i]):
            return nums[i]

def find_encryption_weakness():
    invalid_number = find_first_weakness()
    for i in range(len(nums)):
        cum_sum = nums[i]
        for j in range(i+1, len(nums)):
            cum_sum += nums[j]
            if cum_sum == invalid_number:
                return (i,j)
            if cum_sum > invalid_number:
                break

    return -1
            

def part_2():
    rnge = find_encryption_weakness()
    lst_sec = sorted(nums[rnge[0]:rnge[1]])
    return lst_sec[0] + lst_sec[-1]

print(part_2())
            


    
