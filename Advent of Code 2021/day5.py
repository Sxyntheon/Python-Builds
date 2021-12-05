
#The only hardcoded part are the max y- and x-values and the number of lines in the input


NUMBS = open("day5.txt", "r")

yWert = []

for i in range(1000):
    xWert = []
    for i in range(1000):
        xWert.append(0)
    yWert.append(xWert)

for line in range(500):
    NEXT = next(NUMBS).strip("\n")
    LINE = NEXT.split(",")
    INT = [ int(x) for x in LINE]
    if INT[0] == INT[2]:
        if INT[1] < INT[3]:
            diff = INT[3] - INT[1]
            for x in range(diff+1):
                yWert[INT[1] + x][INT[0]] += 1
        else:
            diff = INT[1] - INT[3]
            for x in range(diff+1):
                yWert[INT[3] + x][INT[0]] += 1
    elif INT[1] == INT[3]:
        if INT[0] < INT[2]:
            diff = INT[2] - INT[0]
            for x in range(diff+1):
                yWert[INT[1]][INT[0] + x] += 1
        else:
            diff = INT[0] - INT[2]
            for x in range(diff+1):
                yWert[INT[1]][INT[2] + x] += 1
    else:
        if INT[1] < INT[3]:
            diff = INT[3] - INT[1]
            if INT[0] < INT[2]:
                for x in range(diff+1):
                    yWert[INT[1] + x][INT[0] + x] += 1
            elif INT[2] < INT[0]:
                for x in range(diff+1):
                    yWert[INT[1] + x][INT[0] - x] += 1
        elif INT[3] < INT[1]:
            diff = INT[1] - INT[3]
            if INT[0] < INT[2]:
                for x in range(diff+1):
                    yWert[INT[1] - x][INT[0] + x] += 1
            elif INT[2] < INT[0]:
                for x in range(diff+1):
                    yWert[INT[1] - x][INT[0] - x] += 1

NUMBS.close()

write = open("day5_output.txt", "w")

write.write(str(yWert))
write.close()

x = 0

for line in yWert:
    for element in line:
        if element > 1:
            x += 1

print(str(x) + " points have a value of 2 or higher")

#print(yWert)