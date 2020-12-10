def read_file(name, read_type = ""):
    f = open("inputs/"+name+".txt", 'r')
    if read_type == "lines":
        lines = f.readlines()
    else:
        lines = f.read()
    f.close()
    return lines
