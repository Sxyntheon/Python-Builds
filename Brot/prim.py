num = input("Gib eine Zahl ein ")

def prim(number):
    teiler = []
    number_minus_1_list = []
    y = int(number) - 1
    x = 0
    while y > 1:
        number_minus_1_list.append(y)
        print(y)
        if int(number) % y == 0:
            x += 1
            teiler.append(y)
        y = y - 1
    if x == 0:
        print("Deine Zahl ist eine Primzahl")
    else:
        print("Deine Zahl ist keine Primzahl, sie hat " + str(x) + " verschiedene Teiler, das sind " + str(teiler).lstrip("[").rstrip("]"))

prim(num)
