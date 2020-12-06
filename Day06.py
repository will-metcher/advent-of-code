f = open("input.txt", "r")
answers = f.read().split("\n\n")
f.close()

def sum_of_any_response():
    total = 0
    for ans in answers:
        unique = set()
        for a in ans:
            if a not in unique and a != "\n":
                unique.add(a)
        total += len(unique)
    return total

def sum_of_every_response():
    total = 0
    for person in answers:
        len_person = len(person.split("\n"))
        person = person.replace("\n", "")
        unique = set(person)
        for ans in unique:
            if person.count(ans) == len_person:
                total += 1
    return total
            

print(sum_of_every_response())
        
        
