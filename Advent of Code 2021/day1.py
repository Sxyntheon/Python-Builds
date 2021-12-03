def getIncreasements(data):
    y = 0
    x = 0
    while y < 1996:
        if int(data[y]) < int(data[y+1]):
            print(data[y])
            x += 1
        y += 1
    print("The value increases " + str(x) + " times")
    
lines = open("day1.txt", "r")

numbs = []

def getIncreasements2(data):
    y = 0
    list = []
    while y < 1997:
        list.append(int(data[y]) + int(data[y+1]) + int(data[y+2]))
        y += 1
    print(len(list))
    getIncreasements(list)

for x in lines:
    numbs.append(x.strip("\n"))

getIncreasements2(numbs)