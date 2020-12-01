import time

start = time.time()

f = open("input.txt", 'r')
entries = f.read().split("\n")
f.close()


def find_sum_1():
    for i, e1 in enumerate(entries):
        for e2, j in enumerate(entries):
            print(e1 + e2)
            if i == j:
                continue
            if int(e1) + int(e2) == 2020:
                return int(e1) * int(e2)
    return 0

def find_sum_2():
    for i, e1 in enumerate(entries):
        for j, e2 in enumerate(entries):
            if i == j:
                continue
            for k, e3 in enumerate(entries):
                if k == j:
                    continue
                if int(e1) + int(e2) + int(e3) == 2020:
                    return int(e1) * int(e2) * int(e3)
    return 0

print(find_sum_2(),"in",time.time()-start)
            

            
