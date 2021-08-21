auswahl = input("a, x oder c-wert berechnen ")

aergebnis = 0
xergebnis = 0
cergebnis = 0
dergebnis = 0

def lösena(x1,c):
    global aergebnis
    aergebnis = x1-c
    print("a = " + str(aergebnis))

if auswahl == "a":
    xwert = int(input("Was ist der x1-Wert? "))
    cwert = int(input("Was ist der c-Wert? "))

    lösena(xwert,cwert)