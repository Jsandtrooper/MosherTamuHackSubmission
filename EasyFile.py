import random
def randomize(file):
    f = open(file,'r')
    text = f.readlines()
    return (text[random.randint(0,len(text)-1)].strip())
def linerize(file):
    f = open(file, 'r')
    temp = f.readlines()
    return [i.strip() for i in temp]
def CSVread(file):
    f = open(file, "r")
    lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip().split(",")
        for j in range(len(lines[i])):
            lines[i][j] = int(lines[i][j])
    return lines

#randomize("Jobs.txt")