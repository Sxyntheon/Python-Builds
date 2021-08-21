import datetime

class Stundenplan:
    weekday = datetime.datetime.today().weekday()
    current_weekday_content = "none"
    def get_weekday(self):
        if self.weekday == 4:
            self.current_weekday_content = Montag.content
    def __init__(self, weekday_count, weekday_name, weekday_content,):
        self.weekday_amount = weekday_count
        self.name = weekday_name
        self.content = weekday_content

Montag = Stundenplan(0, "Montag", "Heute ist Montag, ihr habt heute\n\n(7:55 Uhr) 1. Stunde: Rat\n(8:40 Uhr) 2. Stunde: Bio\n\n(9:25 - 9:45 Uhr) 1. Pause\n\n(9:45 Uhr) 3. Stunde: Deutsch\n(10:30 Uhr) 4. Stunde: Deutsch\n\n(11:15 - 11:35 Uhr) 2. Pause\n\n(11:35 Uhr) 5. Stunde: Reli/PP\n\n(12:20 - 13:20 Uhr) Mittagspause\n\n(13:20) Uhr 6. Stunde: WP1\n(14:05 Uhr) 7. Stunde: Kunst\n(14:50) Uhr 8. Stunde: Kunst")
Dienstag = Stundenplan(1, "Dienstag", "Heute ist Dienstag, ihr habt also\n\n(7:55 Uhr) 1. Stunde: Mathe\n(8:40 Uhr) 2. Stunde: Mathe\n\n(9:25 - 9:45 Uhr) 1. Pause\n\n(9:45 Uhr) 3. Stunde: Englisch\n(10:30 Uhr) 4. Stunde: Englisch\n\n(11:15 - 11:35 Uhr) 2. Pause\n\n(11:35 Uhr) 5. Stunde: WP1\n(12:20) Uhr 6. Stunde: WP1" )
Mittwoch = Stundenplan(2, "Mittwoch", "Heute ist Dienstag, ne warte heute ist schon Mittwoch, dann habt ihr heute\n\n(7:55 Uhr) 1. Stunde: Englisch\n(8:40 Uhr) 2. Stunde: Englisch\n\n(9:25 - 9:45 Uhr) 1. Pause\n\n(9:45 Uhr) 3. Stunde: GL\n(10:30 Uhr) 4. Stunde: GL\n\n(11:15 - 11:35 Uhr) 2. Pause\n\n(11:35 Uhr) 5. Stunde: AW\n\n(12:20 - 13:20 Uhr) Mittagspause\n\n(13:20 Uhr) 6. Stunde: FöFo/WP2\n(14:05 Uhr) 7. Stunde: Sport\n(14:50 Uhr) 8. Stunde: Sport" )
Donnerstag = Stundenplan(3, "Donnerstag", "Wenn heute Donnerstag ist habt ihr\n\n(7:55 Uhr) 1. Stunde: Mathe\n(8:40 Uhr) 2. Stunde: Mathe\n\n(9:25 - 9:45 Uhr) 1. Pause\n\n(9:45 Uhr) 3. Stunde: Deutsch\n(10:30 Uhr) 4. Stunde: Deutsch\n\n(11:15- 11:35 Uhr) 2. Pause\n\n(11:35 Uhr) 5. Stunde: Reli/PP\n\n(12:20 - 13:20) Mittagspause\n\n(13:20 Uhr) 6. Stunde: Bio\n(14:05 Uhr) 7. Stunde: WP2\n(14:50 Uhr) 8. Stunde: WP2")
Freitag = Stundenplan(4, "Freitag", "Die Woche ist fast vorbei, ihr habt heute noch\n\n(7:55 Uhr) 1. Stunde: GL\n(8:40 Uhr) 2. Stunde: GL\n\n(9:25 - 9:45 Uhr) 1. Pause\n\n(9:45 Uhr)3. Stunde: Chemie\n(10:30 Uhr) 4. Stunde: Chemie\n\n(11:15 - 11:35 Uhr) 2. Pause\n\n(11:35 Uhr) 5. Stunde: AW\n(12:20 Uhr) 6. Stunde: Rat" )
Samstag = Stundenplan(5, "Samstag", "Sehr witzig, heute ist Samstag, ihr habt Wochenende.")
Sonntag = Stundenplan(6, "Sonntag", "Lasst mich in Ruhe, ich hab Frei." )

instanz = Stundenplan(0, 0, 0)
instanz.get_weekday()
print(instanz.current_weekday_content)