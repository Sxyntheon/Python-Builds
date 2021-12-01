from datetime import date

birthdays = {
    "22-09" : "Jakob",
    "08-09" : "Simon",
    "27-09" : "Sascha",
    "03-10" : "Torben",
    "05-05" : "Luis",
    "09-05" : "Mats",
    "10-06" : "Benno",
    "06-09" : "Jamie",
    "28-08" : "Aaron",
    "27-05" : "Kilian"
}

birthdays_string = "Die Geburtstage sind:\nLuis: 05.05\nMats: 09.05\Kilian: 27.05\nBenno: 10.06\nAaron: 28.08\n06.09: Jamie\nSimon: 08.09\nJakob: 22.09\nSascha: 27.09\nTorben: 03.10 "

def check_birthday():        #create function to check if birthday was found in dictionary
    today = date.today()
    date_today = today.strftime("%d-%m")
    
    if date_today in birthdays:
        return True
    else:
        return False

def get_birthday():        #create function to get birthday after check_birthday()-function returned True
    today = date.today()
    date_today = today.strftime("%d-%m")

    if check_birthday() == True:
        return [True, birthdays.get(date_today)]
    else:
        print("no birthday found")
        return [False]
        

