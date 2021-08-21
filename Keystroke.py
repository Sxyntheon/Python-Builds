import random

import datetime

def get_time():
    return datetime.datetime.now()

with open("C:\\Users\jakob\Desktop\Py-Projects\keystroke-text.txt", "r", encoding = "utf8") as text:
    words = text.read().splitlines()



i = 0

list = ""

solution = []

n = input("Wie viele Wörter möchtest du schreiben?\n") #asking how many words to add to the list

while i < int(n): #adding as many words to the list as wanted
    word = random.choice(words)
    list += word
    list += " " #adding spaces between the characters
    i += 1
    #print(word)
list = list[:-1] #removing the last space from the string

print("\nDas ist dein Text: " + list)
start = input("\nZum Beginnen ENTER drücken")
time1 = get_time() #get start at the time
result = input("\nGib den Text ein: ")
time2 = get_time() #get time after finish

user_input = result.split()
solution = list.split()

wrong_input = ""

for i in user_input:
    if i not in solution:
        wrong_input += i
        wrong_input += ", "

if result == list:
    print("\nSehr gut!")
else: 
    print("\nNicht ganz, folgende Wörter waren falsch geschrieben: " + wrong_input)

passed_time = str(round(datetime.timedelta.total_seconds(time2 - time1)))

print("\nDu hast " + passed_time + " Sekunden gebraucht")

if int(n)//int(passed_time) == 1:
    print("\nDeine durchschnittliche Geschwindigkeit lag bei 1 Wort pro Sekunde")
else:
    print("\nDeine durchschnittliche Geschwindigkeit lag bei " + str(round(int(n)/int(passed_time), 2)) + " Wörtern pro Sekunde") #devide number of words by seconds passed and round to two decimal places