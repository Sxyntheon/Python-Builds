import random

from datetime import date

names = ["Jakob", "Simon", "Sascha", "Torben", "Luis", "Benno", "Mats", "Kilian", "Aaron"]

date = date.today()





def check_name(names):
    log = open("log.txt", "r")
    date_log = log.readline()
    log.close
    current_date = date.today()
    if str(current_date) == str(date_log):
        print(date_log, current_date)
        return "error"
    else:
        name = random.choice(names)
        return name

def get_name(names):
    name = random.choice(names)
    return name

ehrenmann = check_name(names)