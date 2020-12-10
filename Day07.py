import utils

rules = utils.read_file("day07", "lines")

result = []

def num_bags(bag_name):
    for line in rules:
        if bag_name in line and not line.startswith(bag_name):
            bag = line.split(" ")
            valid = bag[0] + " " + bag[1]
            if valid not in result:
                result.append(valid)
                num_bags(valid)


num_bags("shiny gold")
print(len(result))

def gold_bag_contains(bag_name):
    total = 0
    for line in rules:
        if line.startswith(bag_name):
            bag = line.split(" ")
            if len(bag) == 7:
                return 0
            else:
                for i in range(6,len(bag),4):
                    next_bag = bag[i-1] + " " + bag[i]
                    total += int(bag[i-2]) * (gold_bag_contains(next_bag)+1)
    return total

print(gold_bag_contains("shiny gold"))
            
