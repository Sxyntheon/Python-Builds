input = open("day8.txt", "r")

Input = []

for i in input:
    Input.append(i.strip("\n").split(" | ")[1])

Chars = []
for line in Input:
    Chars.append(line.split(" "))


count = 0

for element in Chars:
    for chars in element:
        if len(chars) == 2:
            count += 1
            print(chars)
        elif len(chars) == 4:
            count += 1
            print(chars)
        elif len(chars) == 3:
            count += 1
            print(chars)
        elif len(chars) == 7:
            count += 1
            print(chars)
print(count)

        
