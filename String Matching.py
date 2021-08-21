string = "Das ist ein Satz mit sieben Wörtern"

string2 = "Dsa is ein Satz mit sieben Wörtern"

result = string2.split()

solution = string.split()

list = ""

for x in result:
    if x in solution:
        print("Yes")
    else:
        list += x
        list += " "

print(list)