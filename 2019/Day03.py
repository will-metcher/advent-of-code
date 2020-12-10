import math

def calc_taxicab_distance(x1, y1, x2, y2):
    return abs(x2-x1) + abs(y2-y1)

def trace_path(path):
    trace = []
    x,y = 0,0
    for step in path:
        d = step[0]
        dist = int(step[1:])
        for i in range(dist):
            if d == "U":
                y -= 1
            elif d == "D":
                y += 1
            elif d == "L":
                x -= 1
            else:
                x += 1
            trace.append((x,y))
    return trace

def find_intersections(x,y):
    return list(set(x).intersection(y))

def find_shortest_intersection():
    f = open("input.txt", "r")
    dirs = f.read()
    f.close()
    dirs = dirs.split("\n")
    w1 = dirs[0].split(",")
    w2 = dirs[1].split(",")

    x = trace_path(w1)
    y = trace_path(w2)
    intersections = find_intersections(x,y)
    
    smallest = math.inf
    for i in intersections:
        dist = calc_taxicab_distance(0,0,i[0],i[1])
        if dist < smallest:
            smallest = dist
    return smallest

def find_shortest_intersection_steps():
    f = open("input.txt", "r")
    dirs = f.read()
    f.close()
    dirs = dirs.split("\n")
    w1 = dirs[0].split(",")
    w2 = dirs[1].split(",")

    x = trace_path(w1)
    y = trace_path(w2)
    intersections = find_intersections(x,y)

    shortest = math.inf
    for i in intersections:
        w1_steps, w2_steps = 1,1
        for a in range(len(x)):
            if x[a] == i:
                break
            w1_steps += 1
            
        for b in range(len(y)):
            if y[b] == i:
                break
            w2_steps += 1
        
        total = w1_steps + w2_steps
        if total < shortest:
            shortest = total
            
    return shortest
                
    
print(find_shortest_intersection_steps())
    





    
    
