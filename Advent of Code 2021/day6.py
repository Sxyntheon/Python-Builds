FILE = open("day6.txt", "r")
Fish = []
NUMBS = FILE.readline()
SPLIT = NUMBS.split(",")
for x in SPLIT:
    Fish.append(int(x))
FILE.close()

for i in range(256):
    new = 0
    counter = 0
    for item in Fish:
        if item >= 1:
            Fish[counter] -= 1
        else:
            Fish [counter] = 6
            new += 1
        counter += 1
    for x in range(new):
        Fish.append(8)
    print(i)
    
print(len(Fish))
