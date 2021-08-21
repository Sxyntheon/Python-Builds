from time import sleep

GREEN = '\033[92m'
ENDCODE = '\033[0m'


x = 1

while x < 100:
    print(f"{GREEN}✓ Test " + str(x) + " passed")
    x += 1
    sleep(0.3)


