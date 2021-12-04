from numpy import transpose

numbs = open("day4.txt", "r")


inst = numbs.readline().replace("\n", "").split(",")

#print(inst)
x = 0
while x < 100:
    table = []
    x += 1
    for y in range(6):
        y = next(numbs).replace("\n", "")
        LINE = y.split(" ")
        if len(y) > 1:
            table.append(LINE)

    tableFLIP = transpose(table)

    for num in inst:
        for line in table:
            for int in line:
                if int == num:
                    #print(table[table.index(line)][line.index(int)])
                    table[table.index(line)][line.index(int)] = "999"
                    print(table[table.index(line)])
                else:
                    print("No match")
    

numbs.close()