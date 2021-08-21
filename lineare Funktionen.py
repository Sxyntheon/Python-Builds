auswahl = input("x, y, a, b-wert berechnen (x/y/a/b)")

yergebnis = 0
xergebnis = 0
aergebnis = 0
bergebnis = 0


def lösenx(a,y,b):
    global yergebnis
    global xergebnis
    xergebnis = (y-b)/a
    yergebnis = a*xergebnis+b
    print("x = " + str(xergebnis))
    print("f(x) = " + str(yergebnis))

def löseny(a,x,b):
    global yergebnis
    global xergebnis
    yergebnis = a*x+b
    xergebnis = (yergebnis-b)/a
    print("f(x) = " + str(yergebnis))
    print("x = " + str(xergebnis))

def lösena(x,y,b):
    global aergebnis
    aergebnis = (y-b)/x
    print("a = " + str(aergebnis))

def lösenb(y,a,x):
    global bergebnis
    bergebnis = y-(x*a)
    print("b = " + str(bergebnis))

if auswahl == "y":
    awert = int(input("Was ist der a-Wert? "))
    xwert = int(input("Was ist der x-Wert? "))
    bwert = int(input("Was ist der b-Wert? "))
    
    
    löseny(awert,xwert,bwert)
    
    input("Drücke eine Taste zum Beenden")

if auswahl == "x":
    awert = int(input("Was ist der a-Wert? "))
    ywert = int(input("Was ist der y-Wert? "))
    bwert = int(input("Was ist der b-Wert? "))

    lösenx(awert,ywert,bwert)

    input("Drücke eine Taste zum Beenden")

if auswahl == "a":
    xwert = int(input("Was ist der x-Wert? "))
    ywert = int(input("Was ist der y-Wert? "))
    bwert = int(input("Was ist der b-Wert? "))

    
    lösena(xwert, ywert, bwert)

    input("Drücke eine Taste zum Beenden")

if auswahl == "b":
    ywert = int(input("Was ist der y-Wert? "))
    awert = int(input("Was ist der a-Wert? "))
    xwert = int(input("Was ist der x-Wert? "))


    lösenb(ywert,awert,xwert)

    input("Drücke eine Taste zum Beenden")