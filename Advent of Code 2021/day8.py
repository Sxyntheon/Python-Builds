input = open("day8.txt", "r")

INPUT = input.split(" ")

count = 0

for i in input:
    if len(i) == 2:
        count += 1
    elif len(i) == 4:
        count += 1
    elif len(i) == 3:
        count += 1
    elif len(i) == 7:
        count += 1
print(count)

        
