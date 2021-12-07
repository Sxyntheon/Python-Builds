input = open("day7.txt", "r")
POS = []

for i in input.readline().split(","):
    POS.append(int(i))

allFuel = []

for value in range(max(POS)):
    Fuel = 0
    for i in POS:
        count = 0
        while i < value:
            i += 1
            count += 1
            Fuel += count
        while i > value:
            i -= 1
            count += 1
            Fuel += count
    allFuel.append(Fuel)


print(min(allFuel))