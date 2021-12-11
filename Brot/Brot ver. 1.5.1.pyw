import discord                  #import libaries

                               
from datetime import datetime, timedelta, date
from time import sleep

import birthday
import stundenplan
import ehrenmann_des_tages as edt

import random

date = date.today()

class colors:
    GREEN = '\033[92m'
    ENDCODE = '\033[0m'


schnickschnackschnuck = ["Schere", "Stein", "Papier"]               #define lists for functions

bot = discord.Client()

tokentxt = open("token.txt", "r")
token = tokentxt.readline()
tokentxt.close()


MyIP = "none"   

process_finished = f"{colors.GREEN}✓ Vorgang abgeschlossen{colors.ENDCODE}"

start_time = datetime.now()

def uptime():
    now_time = datetime.now()
    up_time = timedelta.total_seconds(now_time - start_time)
    return up_time

birthday.check_birthday()
birthday.get_birthday()

@bot.event  	                    #define output when on working state
async def on_ready():
    #if stundenplan.weekday == 2:
    #    print("Weekday Wednesday: " + f"{colors.GREEN}True{colors.ENDCODE}")
    #    await bot.get_channel(804314475112955936).send("Es ist Mittwoch meine Kerle")
    #else:
    #    print("Weekday Wednesday: False")
    if birthday.get_birthday()[0] == True:
        if birthday.get_birthday()[1] == "Jamie":
            await bot.get_channel(837702077365878787).send("Der Kek " + birthday.get_birthday()[1] + " hat heute Geburtstag")
        else:
            await bot.get_channel(837702077365878787).send("Der Bruder " + birthday.get_birthday()[1] + " hat heute Geburtstag")
        print(process_finished)
    else:
        pass
    print(process_finished)
    print("JETZT ONLINE")
    
while True:

    ehrenmann_des_tages_cnt = 0
    
    ey_geile_cnt = 0                    #define counter for "ey geile" command
    @bot.event
    async def on_message(message):          #define what to do when receiving message
        if message.content == "ey hilfe":   #define help command
            await message.channel.send("Hier ist eine Liste mit Befehlen:\n- ey hilfe (Zeigt eine Liste der Befehle)\n- ey bot\n- ey geile\n- ey wie gehts?\n- ey schnick schnack schnuck\n- ey uptime\n- ey send nudes\n- can i get a oh yeah?\n- ey termine\n- ey stundenplan (zeigt den heutigen Stundeplan)\n- ey stundenplan gesamt\n- ey wer ist ehrenbro des tages? (wählt zufällig einen Ehrenmann des Tages aus)\n- ey wer ist der ehrenmann des tages?\n- ey selbstzerstörung\nProbier sie doch einfach mal aus")
        elif message.content == "ey wie gehts?":
            await message.channel.send("Muss ne")
        elif message.content == "ey uptime":
            if round(uptime())//60 == 1:
                await message.channel.send("Online seit " + str(round(uptime())//60) + " Minute")
            else:
                await message.channel.send("Online seit " + str(round(uptime())//60) + " Minuten")
        elif message.content == "ey bot":
            await message.channel.send("Was los?")
        elif message.content == "ey stundenplan":
            await message.channel.send(stundenplan.today_stundenplan)
        #elif message.content == "ey termine":
        #    await message.channel.send("Die nächsten Termine sind:\n\n12.05 Studientag\n\n18.05 Auftaktsveranstaltung für die Betriebsralley\n\n26.05 Deutsch LC Gruppe B\n\n28.05 Mathe LC Gruppe B\n\n31.05 Deutsch LC Gruppe A\n\n04.06 Mathe LC Gruppe A\n\n07.06 mündl. Prüfung E Gruppe B\n\n07-12.06 WP1 LC Gruppe B\n\n14.06 mündl. Prüfung E Gruppe A\n\n14-18.06 WP1 LC Gruppe A")
        #elif message.content == "ey ip":
        #    await message.channel.send("Die aktuelle IP lautet: " + MyIP)
        elif message.content == "ey geburtstage":
            await message.channel.send(birthday.birtdays_string)
        elif message.content == "ey stundenplan gesamt":
            await message.channel.send(stundenplan.Stundenplan_Gesamt_Content)
        elif message.content == "can i get a oh yeah?":
            await message.channel.send("OH YEAH!")
        elif message.content == "ey send nudes":
            await message.channel.send("https://th.bing.com/th/id/OIP.ruwPbKYdddKFFe6V4HQYNgHaJI?w=151&h=186&c=7&o=5&dpr=1.5&pid=1.7")
        elif message.content == "ey wer ist ehrenbro des tages?":
            ehrenmann = edt.check_name(edt.names)
            if str(ehrenmann) == "error":
                await message.channel.send("Der Ehrenbro des Tages wurde heute schon bestimmt!")
                print("error")
            else:
                await message.channel.send("Und der Ehrenbro des Tages ist:")
                print(ehrenmann)
                sleep(5)
                log = open("log.txt", "w")
                log.write(str(date))
                log.close()
                await message.channel.send(ehrenmann)
        elif message.content == "ey wer ist der ehrenbro des tages?":
            global ehrenmann_des_tages_cnt
            ehrenmann_des_tages_cnt = 1
            await message.channel.send("Und der ehrenbro des Tages ist:")
            sleep(5)
            await message.channel.send("Joe")
        elif message.content == "welcher Joe?":
            if ehrenmann_des_tages_cnt == 1:
                await message.channel.send("Joe Mama")
                ehrenmann_des_tages_cnt = 0
                sleep(3)
                await message.channel.send("Boom roasted")
        elif message.content == "ey geile":
            await message.channel.send("ey geiler")
            global ey_geile_cnt
            ey_geile_cnt = 1
        elif message.content == "alleine?":
            if ey_geile_cnt == 1:
                await message.channel.send("ja leider")
                ey_geile_cnt = 2
        elif message.content == "bist du neu in dieser stadt?":
            if ey_geile_cnt == 2:
                await message.channel.send("ne, bin nur neu in diesem Club")
                ey_geile_cnt = 0
        elif message.content == "ey schnick schnack schnuck":
            await message.channel.send("Du hast 10 Sekunden um deine Antwort zu schreiben")
            sleep(10)
            await message.channel.send(random.choice(schnickschnackschnuck))
        elif message.content == "ey selbstzerstörung":
            await message.channel.send("Selbst Zerstörung in:")
            await message.channel.send("10")
            sleep(1)
            await message.channel.send("9")
            sleep(1)
            await message.channel.send("8")
            sleep(1)
            await message.channel.send("7")
            sleep(1)
            await message.channel.send("6")
            sleep(1)
            await message.channel.send("5")
            sleep(1)
            await message.channel.send("4")
            sleep(1)
            await message.channel.send("3")
            sleep(1)
            await message.channel.send("2")
            sleep(1)
            await message.channel.send("1")
            sleep(1)
            await message.channel.send("BOOM!")
            sleep(3)
            await message.channel.send("Bin ich tot?")
    bot.run(token)