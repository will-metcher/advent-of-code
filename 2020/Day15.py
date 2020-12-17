input_string = "5,2,8,16,18,0,1"
turns = 30000000

numbers = {int(i): index for index, i in enumerate(input_string.split(","), start=1)}
all_nums = [int(i) for i in input_string.split(",")]

next_spoken = 0

for n in range(len(numbers) + 1, turns):
    all_nums.append(next_spoken)
    if next_spoken in numbers.keys():
        next_number = n - numbers[next_spoken]
        numbers[next_spoken] = n
        next_spoken = next_number
    else:
        numbers[next_spoken] = n
        next_spoken = 0

print(next_spoken)
