def getCoordinates():
    coordsRaw = open("day2.txt", "r")
    coordsTXT = open("coordsTXT.txt", "w")
    coords = []
    for i in coordsRaw:
        coords.append(i.replace(" ", " += ").strip("\n"))
    print(coords)
    coordsTXT.write(str(coords))

def addCoordinates2():
    forward = 0
    aim = 0
    depth = 0

    forward += 9

    depth += 9*aim

    aim += 3

    aim += 8

    forward += 2

    depth += 2*aim

    aim -=  3

    forward += 5

    depth += 5*aim

    aim -=  8

    aim += 2

    aim += 5

    aim -=  7

    aim += 9

    forward += 4

    depth += 4*aim

    aim -=  5

    aim += 9

    forward += 2

    depth += 2*aim

    forward += 2

    depth += 2*aim

    forward += 8

    depth += 8*aim

    aim += 6

    forward += 2

    depth += 2*aim

    aim -=  9

    aim -=  5

    aim += 2

    forward += 5

    depth += 5*aim

    aim += 8

    forward += 3

    depth += 3*aim

    aim -=  4

    forward += 5

    depth += 5*aim

    forward += 7

    depth += 7*aim

    aim += 8

    aim += 6

    aim -=  7

    aim += 3

    forward += 4

    depth += 4*aim

    aim -=  8

    aim += 5

    aim += 3

    aim += 6

    aim += 8

    forward += 1

    depth += 1*aim

    forward += 9

    depth += 9*aim

    forward += 4

    depth += 4*aim

    aim -=  7

    aim += 4

    forward += 7

    depth += 7*aim

    forward += 3

    depth += 3*aim

    forward += 9

    depth += 9*aim

    aim += 1

    aim += 3

    aim -=  9

    aim += 3

    forward += 9

    depth += 9*aim

    aim -=  6

    aim -=  9

    aim += 8

    aim -=  3

    aim += 1

    aim -=  8

    aim += 8

    aim += 2

    aim += 4

    aim += 4

    aim -=  3

    aim += 6

    aim += 1

    aim += 3

    forward += 1

    depth += 1*aim

    aim -=  5

    forward += 5

    depth += 5*aim

    forward += 8

    depth += 8*aim

    aim += 2

    forward += 6

    depth += 6*aim

    forward += 2

    depth += 2*aim

    aim -=  7

    forward += 6

    depth += 6*aim

    aim += 8

    forward += 6

    depth += 6*aim

    forward += 5

    depth += 5*aim

    aim -=  9

    forward += 5

    depth += 5*aim

    aim -=  5

    forward += 9

    depth += 9*aim

    aim += 2

    aim += 4

    aim += 3

    aim += 8

    forward += 9

    depth += 9*aim

    forward += 6

    depth += 6*aim

    forward += 2

    depth += 2*aim

    aim -=  7

    aim += 7

    aim -=  3

    forward += 4

    depth += 4*aim

    forward += 5

    depth += 5*aim

    aim += 7

    forward += 5

    depth += 5*aim

    aim -=  9

    forward += 6

    depth += 6*aim

    forward += 6

    depth += 6*aim

    forward += 1

    depth += 1*aim

    aim += 6

    forward += 9

    depth += 9*aim

    aim -=  2

    aim += 7

    aim += 8

    aim += 6

    aim -=  5

    aim += 8

    aim += 8

    forward += 7

    depth += 7*aim

    aim += 6

    aim -=  5

    aim += 9

    aim += 3

    forward += 2

    depth += 2*aim

    aim += 4

    forward += 8

    depth += 8*aim

    aim += 5

    aim -=  5

    forward += 7

    depth += 7*aim

    aim -=  2

    aim -=  2

    aim += 4

    forward += 4

    depth += 4*aim

    aim += 5

    aim -=  8

    aim += 2

    forward += 4

    depth += 4*aim

    aim += 9

    forward += 8

    depth += 8*aim

    aim += 5

    aim += 6

    aim += 7

    aim -=  7

    aim -=  5

    aim -=  7

    forward += 7

    depth += 7*aim

    forward += 8

    depth += 8*aim

    aim += 2

    forward += 3

    depth += 3*aim

    aim += 2

    aim += 7

    aim += 4

    aim += 2

    forward += 3

    depth += 3*aim

    forward += 5

    depth += 5*aim

    aim += 3

    aim += 7

    aim -=  7

    aim += 7

    aim -=  5

    forward += 1

    depth += 1*aim

    aim += 8

    aim += 2

    aim -=  4

    aim -=  5

    aim += 8

    forward += 9

    depth += 9*aim

    aim += 3

    aim += 9

    forward += 8

    depth += 8*aim

    forward += 1

    depth += 1*aim

    forward += 1

    depth += 1*aim

    aim += 2

    aim -=  9

    aim += 2

    aim -=  8

    aim += 6

    aim -=  8

    forward += 7

    depth += 7*aim

    aim += 5

    forward += 7

    depth += 7*aim

    aim += 8

    forward += 8

    depth += 8*aim

    aim += 7

    aim -=  9

    aim -=  2

    aim -=  6

    aim += 5

    aim += 9

    forward += 2

    depth += 2*aim

    aim -=  3

    aim += 4

    aim -=  5

    aim -=  4

    aim += 9

    forward += 7

    depth += 7*aim

    forward += 7

    depth += 7*aim

    aim += 3

    forward += 4

    depth += 4*aim

    forward += 9

    depth += 9*aim

    aim -=  8

    forward += 3

    depth += 3*aim

    aim += 1

    forward += 2

    depth += 2*aim

    aim += 7

    aim += 3

    aim += 7

    aim += 7

    forward += 8

    depth += 8*aim

    forward += 4

    depth += 4*aim

    forward += 7

    depth += 7*aim

    aim -=  1

    aim += 4

    aim -=  9

    aim += 2

    aim += 1

    forward += 6

    depth += 6*aim

    aim += 3

    forward += 7

    depth += 7*aim

    forward += 8

    depth += 8*aim

    aim -=  9

    aim -=  2

    aim -=  2

    forward += 7

    depth += 7*aim

    aim -=  2

    aim -=  5

    forward += 5

    depth += 5*aim

    aim += 3

    forward += 8

    depth += 8*aim

    forward += 1

    depth += 1*aim

    aim -=  4

    aim += 6

    aim += 5

    forward += 4

    depth += 4*aim

    aim -=  9

    forward += 8

    depth += 8*aim

    aim -=  4

    aim += 8

    aim += 3

    aim += 3

    aim += 7

    forward += 2

    depth += 2*aim

    forward += 4

    depth += 4*aim

    aim += 9

    aim += 7

    aim += 2

    aim -=  3

    aim -=  3

    forward += 8

    depth += 8*aim

    forward += 7

    depth += 7*aim

    forward += 8

    depth += 8*aim

    aim += 5

    aim -=  5

    forward += 3

    depth += 3*aim

    forward += 6

    depth += 6*aim

    aim -=  7

    aim -=  1

    forward += 2

    depth += 2*aim

    forward += 5

    depth += 5*aim

    aim += 5

    forward += 8

    depth += 8*aim

    aim += 2

    aim += 4

    forward += 2

    depth += 2*aim

    aim += 7

    aim += 3

    aim += 5

    forward += 9

    depth += 9*aim

    aim += 7

    aim += 8

    aim -=  1

    aim -=  2

    aim += 8

    forward += 7

    depth += 7*aim

    forward += 8

    depth += 8*aim

    aim += 8

    forward += 5

    depth += 5*aim

    aim -=  7

    forward += 3

    depth += 3*aim

    aim -=  2

    aim += 7

    forward += 1

    depth += 1*aim

    aim += 2

    aim -=  7

    aim -=  4

    aim += 2

    forward += 1

    depth += 1*aim

    aim -=  5

    forward += 2

    depth += 2*aim

    aim -=  2

    forward += 3

    depth += 3*aim

    forward += 9

    depth += 9*aim

    forward += 2

    depth += 2*aim

    forward += 8

    depth += 8*aim

    forward += 2

    depth += 2*aim

    aim -=  7

    aim += 8

    aim += 7

    forward += 2

    depth += 2*aim

    forward += 7

    depth += 7*aim

    aim += 1

    forward += 2

    depth += 2*aim

    aim -=  1

    aim -=  6

    aim += 3

    aim += 6

    forward += 7

    depth += 7*aim

    aim += 4

    forward += 5

    depth += 5*aim

    forward += 6

    depth += 6*aim

    aim -=  3

    forward += 3

    depth += 3*aim

    aim += 6

    forward += 8

    depth += 8*aim

    aim -=  8

    forward += 4

    depth += 4*aim

    aim += 3

    forward += 3

    depth += 3*aim

    aim += 4

    aim += 7

    forward += 9

    depth += 9*aim

    forward += 2

    depth += 2*aim

    aim -=  2

    forward += 8

    depth += 8*aim

    aim += 6

    forward += 6

    depth += 6*aim

    aim += 9

    aim += 9

    forward += 8

    depth += 8*aim

    aim += 1

    forward += 9

    depth += 9*aim

    aim += 1

    aim += 6

    aim += 8

    aim += 5

    aim += 5

    forward += 3

    depth += 3*aim

    forward += 3

    depth += 3*aim

    aim += 2

    aim += 5

    forward += 9

    depth += 9*aim

    aim += 2

    aim += 8

    aim += 3

    forward += 9

    depth += 9*aim

    aim -=  2

    aim += 4

    aim += 9

    forward += 9

    depth += 9*aim

    forward += 1

    depth += 1*aim

    forward += 5

    depth += 5*aim

    aim -=  9

    aim += 1

    aim += 6

    forward += 6

    depth += 6*aim

    forward += 5

    depth += 5*aim

    forward += 8

    depth += 8*aim

    aim += 2

    forward += 8

    depth += 8*aim

    aim += 4

    aim += 2

    aim += 6

    aim += 6

    aim -=  3

    aim -=  8

    forward += 1

    depth += 1*aim

    aim += 1

    aim -=  8

    aim += 3

    aim += 4

    aim -=  9

    aim -=  1

    aim += 7

    aim += 7

    aim -=  1

    aim -=  2

    forward += 5

    depth += 5*aim

    aim -=  8

    forward += 2

    depth += 2*aim

    aim += 3

    forward += 1

    depth += 1*aim

    aim -=  5

    forward += 6

    depth += 6*aim

    forward += 2

    depth += 2*aim

    aim += 6

    aim -=  2

    forward += 2

    depth += 2*aim

    forward += 1

    depth += 1*aim

    aim += 3

    forward += 4

    depth += 4*aim

    aim -=  8

    forward += 5

    depth += 5*aim

    aim += 4

    forward += 2

    depth += 2*aim

    aim += 8

    aim += 7

    aim -=  7

    aim += 8

    forward += 1

    depth += 1*aim

    aim += 4

    aim -=  9

    aim += 6

    aim -=  6

    aim -=  6

    aim += 2

    forward += 1

    depth += 1*aim

    forward += 8

    depth += 8*aim

    aim += 6

    aim -=  3

    aim += 7

    forward += 9

    depth += 9*aim

    aim -=  1

    aim -=  4

    forward += 7

    depth += 7*aim

    aim += 7

    forward += 1

    depth += 1*aim

    aim += 6

    aim += 4

    aim += 7

    aim += 8

    aim += 8

    forward += 4

    depth += 4*aim

    aim += 6

    aim += 6

    aim += 5

    forward += 6

    depth += 6*aim

    aim -=  9

    aim -=  3

    aim += 4

    forward += 8

    depth += 8*aim

    aim += 7

    forward += 6

    depth += 6*aim

    aim -=  3

    forward += 1

    depth += 1*aim

    forward += 1

    depth += 1*aim

    aim += 8

    forward += 7

    depth += 7*aim

    forward += 4

    depth += 4*aim

    forward += 6

    depth += 6*aim

    aim -=  1

    forward += 7

    depth += 7*aim

    aim -=  8

    forward += 2

    depth += 2*aim

    forward += 6

    depth += 6*aim

    forward += 8

    depth += 8*aim

    aim += 9

    aim += 8

    aim -=  9

    aim -=  4

    aim -=  2

    forward += 2

    depth += 2*aim

    forward += 8

    depth += 8*aim

    aim -=  2

    forward += 3

    depth += 3*aim

    forward += 2

    depth += 2*aim

    aim -=  2

    aim -=  5

    aim -=  8

    forward += 4

    depth += 4*aim

    forward += 8

    depth += 8*aim

    forward += 3

    depth += 3*aim

    aim -=  5

    aim += 1

    forward += 2

    depth += 2*aim

    aim += 7

    aim += 8

    forward += 3

    depth += 3*aim

    aim -=  1

    forward += 5

    depth += 5*aim

    forward += 7

    depth += 7*aim

    forward += 9

    depth += 9*aim

    aim -=  7

    forward += 4

    depth += 4*aim

    aim += 4

    aim -=  2

    forward += 4

    depth += 4*aim

    forward += 5

    depth += 5*aim

    forward += 3

    depth += 3*aim

    aim -=  9

    forward += 6

    depth += 6*aim

    forward += 8

    depth += 8*aim

    aim += 9

    aim += 1

    forward += 1

    depth += 1*aim

    aim += 5

    aim += 2

    forward += 9

    depth += 9*aim

    aim += 2

    aim -=  9

    aim += 1

    forward += 5

    depth += 5*aim

    forward += 8

    depth += 8*aim

    aim -=  2

    forward += 6

    depth += 6*aim

    aim += 4

    aim += 9

    forward += 4

    depth += 4*aim

    forward += 1

    depth += 1*aim

    aim += 3

    aim += 3

    aim -=  5

    forward += 5

    depth += 5*aim

    aim += 6

    forward += 3

    depth += 3*aim

    aim += 2

    forward += 8

    depth += 8*aim

    aim += 7

    aim += 2

    aim += 1

    forward += 2

    depth += 2*aim

    aim -=  5

    forward += 9

    depth += 9*aim

    forward += 3

    depth += 3*aim

    forward += 5

    depth += 5*aim

    aim += 4

    aim -=  7

    forward += 6

    depth += 6*aim

    aim += 3

    forward += 1

    depth += 1*aim

    forward += 7

    depth += 7*aim

    forward += 1

    depth += 1*aim

    aim -=  4

    aim += 2

    aim += 7

    aim -=  9

    forward += 9

    depth += 9*aim

    aim += 8

    aim += 1

    aim -=  2

    aim += 3

    forward += 7

    depth += 7*aim

    aim += 8

    aim += 5

    aim += 5

    aim -=  8

    forward += 1

    depth += 1*aim

    aim += 5

    forward += 8

    depth += 8*aim

    aim -=  7

    aim += 1

    forward += 9

    depth += 9*aim

    aim += 4

    forward += 8

    depth += 8*aim

    forward += 5

    depth += 5*aim

    forward += 7

    depth += 7*aim

    forward += 8

    depth += 8*aim

    forward += 3

    depth += 3*aim

    aim -=  9

    forward += 3

    depth += 3*aim

    aim += 7

    aim += 5

    aim -=  8

    forward += 3

    depth += 3*aim

    aim -=  6

    forward += 8

    depth += 8*aim

    aim -=  3

    aim += 5

    forward += 5

    depth += 5*aim

    forward += 6

    depth += 6*aim

    forward += 4

    depth += 4*aim

    forward += 3

    depth += 3*aim

    forward += 8

    depth += 8*aim

    aim -=  9

    forward += 2

    depth += 2*aim

    aim += 6

    aim += 4

    aim += 5

    forward += 7

    depth += 7*aim

    aim += 2

    aim -=  5

    forward += 2

    depth += 2*aim

    forward += 5

    depth += 5*aim

    aim += 9

    forward += 8

    depth += 8*aim

    aim += 8

    forward += 6

    depth += 6*aim

    aim += 9

    aim += 7

    aim -=  9

    forward += 3

    depth += 3*aim

    forward += 3

    depth += 3*aim

    aim -=  5

    aim += 2

    forward += 5

    depth += 5*aim

    aim += 6

    aim += 6

    aim += 2

    aim += 3

    aim += 4

    forward += 7

    depth += 7*aim

    aim -=  1

    aim += 7

    forward += 7

    depth += 7*aim

    aim -=  1

    forward += 3

    depth += 3*aim

    aim -=  6

    aim += 7

    aim += 5

    forward += 9

    depth += 9*aim

    forward += 2

    depth += 2*aim

    aim += 5

    forward += 9

    depth += 9*aim

    aim += 5

    forward += 9

    depth += 9*aim

    forward += 1

    depth += 1*aim

    aim += 4

    forward += 9

    depth += 9*aim

    aim += 5

    forward += 8

    depth += 8*aim

    aim += 6

    aim += 4

    aim += 5

    forward += 9

    depth += 9*aim

    aim += 1

    forward += 6

    depth += 6*aim

    forward += 9

    depth += 9*aim

    aim += 1

    aim += 1

    aim -=  2

    forward += 5

    depth += 5*aim

    forward += 3

    depth += 3*aim

    aim += 4

    aim -=  8

    forward += 8

    depth += 8*aim

    aim += 2

    forward += 3

    depth += 3*aim

    forward += 1

    depth += 1*aim

    aim += 7

    forward += 6

    depth += 6*aim

    forward += 5

    depth += 5*aim

    aim -=  7

    aim -=  8

    aim += 5

    aim -=  3

    aim += 8

    forward += 6

    depth += 6*aim

    forward += 5

    depth += 5*aim

    forward += 6

    depth += 6*aim

    aim -=  1

    aim -=  8

    aim -=  7

    aim += 5

    forward += 3

    depth += 3*aim

    forward += 9

    depth += 9*aim

    aim -=  9

    aim -=  4

    aim -=  7

    aim -=  8

    forward += 7

    depth += 7*aim

    forward += 3

    depth += 3*aim

    forward += 9

    depth += 9*aim

    aim += 7

    forward += 3

    depth += 3*aim

    aim += 6

    forward += 9

    depth += 9*aim

    aim += 1

    forward += 3

    depth += 3*aim

    aim += 1

    forward += 8

    depth += 8*aim

    forward += 7

    depth += 7*aim

    aim += 2

    forward += 1

    depth += 1*aim

    forward += 6

    depth += 6*aim

    forward += 7

    depth += 7*aim

    aim += 3

    aim += 2

    aim += 1

    forward += 7

    depth += 7*aim

    forward += 4

    depth += 4*aim

    aim += 6

    aim -=  4

    forward += 4

    depth += 4*aim

    forward += 9

    depth += 9*aim

    forward += 3

    depth += 3*aim

    aim += 1

    aim -=  2

    aim += 3

    aim += 5

    forward += 7

    depth += 7*aim

    forward += 5

    depth += 5*aim

    aim -=  1

    aim += 2

    aim += 3

    aim += 8

    forward += 1

    depth += 1*aim

    aim += 4

    forward += 5

    depth += 5*aim

    aim += 5

    aim -=  6

    aim += 6

    aim += 8

    forward += 1

    depth += 1*aim

    forward += 9

    depth += 9*aim

    aim -=  5

    forward += 2

    depth += 2*aim

    aim += 9

    aim += 5

    aim += 1

    aim += 4

    aim += 9

    aim += 8

    forward += 2

    depth += 2*aim

    forward += 4

    depth += 4*aim

    aim -=  2

    forward += 3

    depth += 3*aim

    aim += 8

    aim += 5

    aim -=  5

    forward += 8

    depth += 8*aim

    aim -=  2

    aim += 8

    aim -=  3

    forward += 7

    depth += 7*aim

    aim += 7

    forward += 8

    depth += 8*aim

    aim += 7

    aim += 3

    aim -=  6

    forward += 5

    depth += 5*aim

    aim -=  4

    aim -=  5

    forward += 9

    depth += 9*aim

    forward += 6

    depth += 6*aim

    aim += 9

    forward += 5

    depth += 5*aim

    aim += 5

    aim += 3

    forward += 2

    depth += 2*aim

    aim += 1

    aim -=  9

    aim -=  8

    aim += 6

    aim += 1

    forward += 9

    depth += 9*aim

    forward += 4

    depth += 4*aim

    forward += 2

    depth += 2*aim

    aim -=  1

    forward += 5

    depth += 5*aim

    forward += 9

    depth += 9*aim

    aim -=  5

    forward += 8

    depth += 8*aim

    forward += 4

    depth += 4*aim

    aim += 4

    aim += 4

    aim += 2

    forward += 1

    depth += 1*aim

    forward += 7

    depth += 7*aim

    aim += 9

    forward += 4

    depth += 4*aim

    aim += 5

    aim += 4

    aim += 7

    aim += 2

    forward += 9

    depth += 9*aim

    aim += 3

    forward += 6

    depth += 6*aim

    forward += 3

    depth += 3*aim

    aim += 9

    aim += 3

    aim += 4

    aim += 9

    aim += 9

    aim -=  6

    aim += 5

    aim -=  4

    aim += 1

    aim += 1

    forward += 9

    depth += 9*aim

    forward += 7

    depth += 7*aim

    aim += 9

    forward += 4

    depth += 4*aim

    aim += 8

    aim += 7

    forward += 7

    depth += 7*aim

    forward += 4

    depth += 4*aim

    aim -=  2

    aim -=  5

    forward += 2

    depth += 2*aim

    forward += 7

    depth += 7*aim

    aim += 1

    forward += 6

    depth += 6*aim

    forward += 6

    depth += 6*aim

    forward += 3

    depth += 3*aim

    forward += 8

    depth += 8*aim

    aim += 2

    aim -=  2

    forward += 7

    depth += 7*aim

    aim -=  5

    aim += 1

    aim += 5

    forward += 8

    depth += 8*aim

    aim += 6

    forward += 8

    depth += 8*aim

    aim += 5

    aim += 4

    aim += 6

    forward += 5

    depth += 5*aim

    aim += 1

    forward += 9

    depth += 9*aim

    forward += 8

    depth += 8*aim

    aim -=  5

    aim += 6

    forward += 5

    depth += 5*aim

    aim -=  5

    aim += 4

    forward += 1

    depth += 1*aim

    aim += 2

    aim += 5

    aim += 3

    forward += 2

    depth += 2*aim

    aim += 9

    forward += 1

    depth += 1*aim

    forward += 1

    depth += 1*aim

    forward += 1

    depth += 1*aim

    forward += 8

    depth += 8*aim

    forward += 2

    depth += 2*aim

    aim += 8

    aim += 6

    aim -=  1

    forward += 6

    depth += 6*aim

    aim += 3

    aim += 4

    aim -=  9

    aim += 3

    aim += 3

    aim -=  7

    aim += 4

    forward += 4

    depth += 4*aim

    forward += 9

    depth += 9*aim

    aim += 3

    aim += 8

    forward += 5

    depth += 5*aim

    aim += 3

    aim += 6

    aim += 7

    forward += 1

    depth += 1*aim

    aim -=  2

    forward += 8

    depth += 8*aim

    aim += 1

    aim += 4

    aim -=  9

    forward += 9

    depth += 9*aim

    aim -=  4

    aim -=  2

    forward += 3

    depth += 3*aim

    forward += 4

    depth += 4*aim

    aim += 2

    aim += 2

    aim += 6

    forward += 6

    depth += 6*aim

    forward += 8

    depth += 8*aim

    aim += 6

    aim -=  6

    aim += 5

    forward += 1

    depth += 1*aim

    aim += 4

    aim -=  9

    forward += 1

    depth += 1*aim

    forward += 3

    depth += 3*aim

    aim += 1

    aim += 4

    aim -=  6

    forward += 5

    depth += 5*aim

    forward += 6

    depth += 6*aim

    aim -=  9

    aim -=  9

    aim += 2

    aim -=  6

    forward += 1

    depth += 1*aim

    forward += 2

    depth += 2*aim

    forward += 3

    depth += 3*aim

    forward += 3

    depth += 3*aim

    forward += 6

    depth += 6*aim

    aim -=  2

    aim += 8

    aim += 9

    forward += 7

    depth += 7*aim

    aim -=  1

    aim -=  3

    aim += 2

    forward += 3

    depth += 3*aim

    aim += 8

    forward += 9

    depth += 9*aim

    aim += 3

    forward += 6

    depth += 6*aim

    aim -=  2

    forward += 7

    depth += 7*aim

    aim += 2

    forward += 5

    depth += 5*aim

    aim += 4

    aim += 2

    aim -=  8

    forward += 3

    depth += 3*aim

    forward += 5

    depth += 5*aim

    forward += 9

    depth += 9*aim

    forward += 5

    depth += 5*aim

    forward += 3

    depth += 3*aim

    aim -=  9

    aim += 7

    forward += 4

    depth += 4*aim

    forward += 2

    depth += 2*aim

    forward += 7

    depth += 7*aim

    aim += 5

    aim -=  6

    aim -=  6

    forward += 8

    depth += 8*aim

    aim += 2

    forward += 1

    depth += 1*aim

    aim -=  1

    aim -=  9

    aim -=  8

    aim -=  3

    aim -=  4

    aim += 2

    aim -=  7

    aim += 4

    aim -=  5

    aim += 1

    aim -=  9

    aim += 5

    aim += 9

    aim += 4

    aim -=  2

    aim += 8

    aim -=  2

    aim -=  7

    aim -=  9

    forward += 4

    depth += 4*aim

    forward += 2

    depth += 2*aim

    forward += 1

    depth += 1*aim

    forward += 6

    depth += 6*aim

    forward += 8

    depth += 8*aim

    aim -=  5

    forward += 5

    depth += 5*aim

    forward += 5

    depth += 5*aim

    aim += 4

    aim -=  6

    forward += 3

    depth += 3*aim

    aim += 9

    aim += 7

    forward += 4

    depth += 4*aim

    aim += 3

    aim -=  1

    forward += 4

    depth += 4*aim

    aim += 2

    aim += 6

    aim -=  3

    aim -=  1

    aim += 9

    aim += 7

    aim += 9

    forward += 3

    depth += 3*aim

    forward += 8

    depth += 8*aim

    aim += 8

    aim -=  7

    aim -=  6

    aim += 2

    aim += 9

    aim += 1

    aim += 9

    forward += 6

    depth += 6*aim

    aim -=  4

    aim += 3

    forward += 5

    depth += 5*aim

    aim -=  3

    aim -=  9

    aim -=  8

    forward += 6

    depth += 6*aim

    aim += 8

    forward += 6

    depth += 6*aim

    forward += 6

    depth += 6*aim

    forward += 5

    depth += 5*aim

    aim -=  4

    aim += 4

    aim -=  6

    aim -=  4

    forward += 2

    depth += 2*aim

    aim += 5

    forward += 9

    depth += 9*aim

    aim -=  7

    aim -=  6

    aim += 4

    forward += 7

    depth += 7*aim

    forward += 6

    depth += 6*aim

    aim -=  2

    aim += 8

    aim += 6

    forward += 5

    depth += 5*aim

    aim -=  2

    forward += 5

    depth += 5*aim

    forward += 1

    depth += 1*aim

    aim -=  9

    aim += 8

    forward += 7

    depth += 7*aim

    aim -=  4

    forward += 8

    depth += 8*aim

    aim += 4

    forward += 3

    depth += 3*aim

    forward += 3

    depth += 3*aim

    aim += 9

    forward += 4

    depth += 4*aim

    forward += 9

    depth += 9*aim

    aim -=  8

    forward += 7

    depth += 7*aim

    forward += 3

    depth += 3*aim

    forward += 9

    depth += 9*aim

    forward += 4

    depth += 4*aim

    aim -=  3

    forward += 2

    depth += 2*aim

    forward += 7

    depth += 7*aim

    solution = depth * forward

    print(solution)

def addCoordinates():
    forward = 0
    up = 0
    down = 0

    forward += 9

    down += 3

    down += 8

    forward += 2

    up += 3

    forward += 5

    up += 8

    down += 2

    down += 5

    up += 7

    down += 9

    forward += 4

    up += 5

    down += 9

    forward += 2

    forward += 2

    forward += 8

    down += 6

    forward += 2

    up += 9

    up += 5

    down += 2

    forward += 5

    down += 8

    forward += 3

    up += 4

    forward += 5

    forward += 7

    down += 8

    down += 6

    up += 7

    down += 3

    forward += 4

    up += 8

    down += 5

    down += 3

    down += 6

    down += 8

    forward += 1

    forward += 9

    forward += 4

    up += 7

    down += 4

    forward += 7

    forward += 3

    forward += 9

    down += 1

    down += 3

    up += 9

    down += 3

    forward += 9

    up += 6

    up += 9

    down += 8

    up += 3

    down += 1

    up += 8

    down += 8

    down += 2

    down += 4

    down += 4

    up += 3

    down += 6

    down += 1

    down += 3

    forward += 1

    up += 5

    forward += 5

    forward += 8

    down += 2

    forward += 6

    forward += 2

    up += 7

    forward += 6

    down += 8

    forward += 6

    forward += 5

    up += 9

    forward += 5

    up += 5

    forward += 9

    down += 2

    down += 4

    down += 3

    down += 8

    forward += 9

    forward += 6

    forward += 2

    up += 7

    down += 7

    up += 3

    forward += 4

    forward += 5

    down += 7

    forward += 5

    up += 9

    forward += 6

    forward += 6

    forward += 1

    down += 6

    forward += 9

    up += 2

    down += 7

    down += 8

    down += 6

    up += 5

    down += 8

    down += 8

    forward += 7

    down += 6

    up += 5

    down += 9

    down += 3

    forward += 2

    down += 4

    forward += 8

    down += 5

    up += 5

    forward += 7

    up += 2

    up += 2

    down += 4

    forward += 4

    down += 5

    up += 8

    down += 2

    forward += 4

    down += 9

    forward += 8

    down += 5

    down += 6

    down += 7

    up += 7

    up += 5

    up += 7

    forward += 7

    forward += 8

    down += 2

    forward += 3

    down += 2

    down += 7

    down += 4

    down += 2

    forward += 3

    forward += 5

    down += 3

    down += 7

    up += 7

    down += 7

    up += 5

    forward += 1

    down += 8

    down += 2

    up += 4

    up += 5

    down += 8

    forward += 9

    down += 3

    down += 9

    forward += 8

    forward += 1

    forward += 1

    down += 2

    up += 9

    down += 2

    up += 8

    down += 6

    up += 8

    forward += 7

    down += 5

    forward += 7

    down += 8

    forward += 8

    down += 7

    up += 9

    up += 2

    up += 6

    down += 5

    down += 9

    forward += 2

    up += 3

    down += 4

    up += 5

    up += 4

    down += 9

    forward += 7

    forward += 7

    down += 3

    forward += 4

    forward += 9

    up += 8

    forward += 3

    down += 1

    forward += 2

    down += 7

    down += 3

    down += 7

    down += 7

    forward += 8

    forward += 4

    forward += 7

    up += 1

    down += 4

    up += 9

    down += 2

    down += 1

    forward += 6

    down += 3

    forward += 7

    forward += 8

    up += 9

    up += 2

    up += 2

    forward += 7

    up += 2

    up += 5

    forward += 5

    down += 3

    forward += 8

    forward += 1

    up += 4

    down += 6

    down += 5

    forward += 4

    up += 9

    forward += 8

    up += 4

    down += 8

    down += 3

    down += 3

    down += 7

    forward += 2

    forward += 4

    down += 9

    down += 7

    down += 2

    up += 3

    up += 3

    forward += 8

    forward += 7

    forward += 8

    down += 5

    up += 5

    forward += 3

    forward += 6

    up += 7

    up += 1

    forward += 2

    forward += 5

    down += 5

    forward += 8

    down += 2

    down += 4

    forward += 2

    down += 7

    down += 3

    down += 5

    forward += 9

    down += 7

    down += 8

    up += 1

    up += 2

    down += 8

    forward += 7

    forward += 8

    down += 8

    forward += 5

    up += 7

    forward += 3

    up += 2

    down += 7

    forward += 1

    down += 2

    up += 7

    up += 4

    down += 2

    forward += 1

    up += 5

    forward += 2

    up += 2

    forward += 3

    forward += 9

    forward += 2

    forward += 8

    forward += 2

    up += 7

    down += 8

    down += 7

    forward += 2

    forward += 7

    down += 1

    forward += 2

    up += 1

    up += 6

    down += 3

    down += 6

    forward += 7

    down += 4

    forward += 5

    forward += 6

    up += 3

    forward += 3

    down += 6

    forward += 8

    up += 8

    forward += 4

    down += 3

    forward += 3

    down += 4

    down += 7

    forward += 9

    forward += 2

    up += 2

    forward += 8

    down += 6

    forward += 6

    down += 9

    down += 9

    forward += 8

    down += 1

    forward += 9

    down += 1

    down += 6

    down += 8

    down += 5

    down += 5

    forward += 3

    forward += 3

    down += 2

    down += 5

    forward += 9

    down += 2

    down += 8

    down += 3

    forward += 9

    up += 2

    down += 4

    down += 9

    forward += 9

    forward += 1

    forward += 5

    up += 9

    down += 1

    down += 6

    forward += 6

    forward += 5

    forward += 8

    down += 2

    forward += 8

    down += 4

    down += 2

    down += 6

    down += 6

    up += 3

    up += 8

    forward += 1

    down += 1

    up += 8

    down += 3

    down += 4

    up += 9

    up += 1

    down += 7

    down += 7

    up += 1

    up += 2

    forward += 5

    up += 8

    forward += 2

    down += 3

    forward += 1

    up += 5

    forward += 6

    forward += 2

    down += 6

    up += 2

    forward += 2

    forward += 1

    down += 3

    forward += 4

    up += 8

    forward += 5

    down += 4

    forward += 2

    down += 8

    down += 7

    up += 7

    down += 8

    forward += 1

    down += 4

    up += 9

    down += 6

    up += 6

    up += 6

    down += 2

    forward += 1

    forward += 8

    down += 6

    up += 3

    down += 7

    forward += 9

    up += 1

    up += 4

    forward += 7

    down += 7

    forward += 1

    down += 6

    down += 4

    down += 7

    down += 8

    down += 8

    forward += 4

    down += 6

    down += 6

    down += 5

    forward += 6

    up += 9

    up += 3

    down += 4

    forward += 8

    down += 7

    forward += 6

    up += 3

    forward += 1

    forward += 1

    down += 8

    forward += 7

    forward += 4

    forward += 6

    up += 1

    forward += 7

    up += 8

    forward += 2

    forward += 6

    forward += 8

    down += 9

    down += 8

    up += 9

    up += 4

    up += 2

    forward += 2

    forward += 8

    up += 2

    forward += 3

    forward += 2

    up += 2

    up += 5

    up += 8

    forward += 4

    forward += 8

    forward += 3

    up += 5

    down += 1

    forward += 2

    down += 7

    down += 8

    forward += 3

    up += 1

    forward += 5

    forward += 7

    forward += 9

    up += 7

    forward += 4

    down += 4

    up += 2

    forward += 4

    forward += 5

    forward += 3

    up += 9

    forward += 6

    forward += 8

    down += 9

    down += 1

    forward += 1

    down += 5

    down += 2

    forward += 9

    down += 2

    up += 9

    down += 1

    forward += 5

    forward += 8

    up += 2

    forward += 6

    down += 4

    down += 9

    forward += 4

    forward += 1

    down += 3

    down += 3

    up += 5

    forward += 5

    down += 6

    forward += 3

    down += 2

    forward += 8

    down += 7

    down += 2

    down += 1

    forward += 2

    up += 5

    forward += 9

    forward += 3

    forward += 5

    down += 4

    up += 7

    forward += 6

    down += 3

    forward += 1

    forward += 7

    forward += 1

    up += 4

    down += 2

    down += 7

    up += 9

    forward += 9

    down += 8

    down += 1

    up += 2

    down += 3

    forward += 7

    down += 8

    down += 5

    down += 5

    up += 8

    forward += 1

    down += 5

    forward += 8

    up += 7

    down += 1

    forward += 9

    down += 4

    forward += 8

    forward += 5

    forward += 7

    forward += 8

    forward += 3

    up += 9

    forward += 3

    down += 7

    down += 5

    up += 8

    forward += 3

    up += 6

    forward += 8

    up += 3

    down += 5

    forward += 5

    forward += 6

    forward += 4

    forward += 3

    forward += 8

    up += 9

    forward += 2

    down += 6

    down += 4

    down += 5

    forward += 7

    down += 2

    up += 5

    forward += 2

    forward += 5

    down += 9

    forward += 8

    down += 8

    forward += 6

    down += 9

    down += 7

    up += 9

    forward += 3

    forward += 3

    up += 5

    down += 2

    forward += 5

    down += 6

    down += 6

    down += 2

    down += 3

    down += 4

    forward += 7

    up += 1

    down += 7

    forward += 7

    up += 1

    forward += 3

    up += 6

    down += 7

    down += 5

    forward += 9

    forward += 2

    down += 5

    forward += 9

    down += 5

    forward += 9

    forward += 1

    down += 4

    forward += 9

    down += 5

    forward += 8

    down += 6

    down += 4

    down += 5

    forward += 9

    down += 1

    forward += 6

    forward += 9

    down += 1

    down += 1

    up += 2

    forward += 5

    forward += 3

    down += 4

    up += 8

    forward += 8

    down += 2

    forward += 3

    forward += 1

    down += 7

    forward += 6

    forward += 5

    up += 7

    up += 8

    down += 5

    up += 3

    down += 8

    forward += 6

    forward += 5

    forward += 6

    up += 1

    up += 8

    up += 7

    down += 5

    forward += 3

    forward += 9

    up += 9

    up += 4

    up += 7

    up += 8

    forward += 7

    forward += 3

    forward += 9

    down += 7

    forward += 3

    down += 6

    forward += 9

    down += 1

    forward += 3

    down += 1

    forward += 8

    forward += 7

    down += 2

    forward += 1

    forward += 6

    forward += 7

    down += 3

    down += 2

    down += 1

    forward += 7

    forward += 4

    down += 6

    up += 4

    forward += 4

    forward += 9

    forward += 3

    down += 1

    up += 2

    down += 3

    down += 5

    forward += 7

    forward += 5

    up += 1

    down += 2

    down += 3

    down += 8

    forward += 1

    down += 4

    forward += 5

    down += 5

    up += 6

    down += 6

    down += 8

    forward += 1

    forward += 9

    up += 5

    forward += 2

    down += 9

    down += 5

    down += 1

    down += 4

    down += 9

    down += 8

    forward += 2

    forward += 4

    up += 2

    forward += 3

    down += 8

    down += 5

    up += 5

    forward += 8

    up += 2

    down += 8

    up += 3

    forward += 7

    down += 7

    forward += 8

    down += 7

    down += 3

    up += 6

    forward += 5

    up += 4

    up += 5

    forward += 9

    forward += 6

    down += 9

    forward += 5

    down += 5

    down += 3

    forward += 2

    down += 1

    up += 9

    up += 8

    down += 6

    down += 1

    forward += 9

    forward += 4

    forward += 2

    up += 1

    forward += 5

    forward += 9

    up += 5

    forward += 8

    forward += 4

    down += 4

    down += 4

    down += 2

    forward += 1

    forward += 7

    down += 9

    forward += 4

    down += 5

    down += 4

    down += 7

    down += 2

    forward += 9

    down += 3

    forward += 6

    forward += 3

    down += 9

    down += 3

    down += 4

    down += 9

    down += 9

    up += 6

    down += 5

    up += 4

    down += 1

    down += 1

    forward += 9

    forward += 7

    down += 9

    forward += 4

    down += 8

    down += 7

    forward += 7

    forward += 4

    up += 2

    up += 5

    forward += 2

    forward += 7

    down += 1

    forward += 6

    forward += 6

    forward += 3

    forward += 8

    down += 2

    up += 2

    forward += 7

    up += 5

    down += 1

    down += 5

    forward += 8

    down += 6

    forward += 8

    down += 5

    down += 4

    down += 6

    forward += 5

    down += 1

    forward += 9

    forward += 8

    up += 5

    down += 6

    forward += 5

    up += 5

    down += 4

    forward += 1

    down += 2

    down += 5

    down += 3

    forward += 2

    down += 9

    forward += 1

    forward += 1

    forward += 1

    forward += 8

    forward += 2

    down += 8

    down += 6

    up += 1

    forward += 6

    down += 3

    down += 4

    up += 9

    down += 3

    down += 3

    up += 7

    down += 4

    forward += 4

    forward += 9

    down += 3

    down += 8

    forward += 5

    down += 3

    down += 6

    down += 7

    forward += 1

    up += 2

    forward += 8

    down += 1

    down += 4

    up += 9

    forward += 9

    up += 4

    up += 2

    forward += 3

    forward += 4

    down += 2

    down += 2

    down += 6

    forward += 6

    forward += 8

    down += 6

    up += 6

    down += 5

    forward += 1

    down += 4

    up += 9

    forward += 1

    forward += 3

    down += 1

    down += 4

    up += 6

    forward += 5

    forward += 6

    up += 9

    up += 9

    down += 2

    up += 6

    forward += 1

    forward += 2

    forward += 3

    forward += 3

    forward += 6

    up += 2

    down += 8

    down += 9

    forward += 7

    up += 1

    up += 3

    down += 2

    forward += 3

    down += 8

    forward += 9

    down += 3

    forward += 6

    up += 2

    forward += 7

    down += 2

    forward += 5

    down += 4

    down += 2

    up += 8

    forward += 3

    forward += 5

    forward += 9

    forward += 5

    forward += 3

    up += 9

    down += 7

    forward += 4

    forward += 2

    forward += 7

    down += 5

    up += 6

    up += 6

    forward += 8

    down += 2

    forward += 1

    up += 1

    up += 9

    up += 8

    up += 3

    up += 4

    down += 2

    up += 7

    down += 4

    up += 5

    down += 1

    up += 9

    down += 5

    down += 9

    down += 4

    up += 2

    down += 8

    up += 2

    up += 7

    up += 9

    forward += 4

    forward += 2

    forward += 1

    forward += 6

    forward += 8

    up += 5

    forward += 5

    forward += 5

    down += 4

    up += 6

    forward += 3

    down += 9

    down += 7

    forward += 4

    down += 3

    up += 1

    forward += 4

    down += 2

    down += 6

    up += 3

    up += 1

    down += 9

    down += 7

    down += 9

    forward += 3

    forward += 8

    down += 8

    up += 7

    up += 6

    down += 2

    down += 9

    down += 1

    down += 9

    forward += 6

    up += 4

    down += 3

    forward += 5

    up += 3

    up += 9

    up += 8

    forward += 6

    down += 8

    forward += 6

    forward += 6

    forward += 5

    up += 4

    down += 4

    up += 6

    up += 4

    forward += 2

    down += 5

    forward += 9

    up += 7

    up += 6

    down += 4

    forward += 7

    forward += 6

    up += 2

    down += 8

    down += 6

    forward += 5

    up += 2

    forward += 5

    forward += 1

    up += 9

    down += 8

    forward += 7

    up += 4

    forward += 8

    down += 4

    forward += 3

    forward += 3

    down += 9

    forward += 4

    forward += 9

    up += 8

    forward += 7

    forward += 3

    forward += 9

    forward += 4

    up += 3

    forward += 2

    forward += 7

    down -= up

    solution = down*forward

    print(solution)

addCoordinates()
addCoordinates2()