from datetime import date

today = date.today()

weekday = today.weekday()

Stundenplan_Gesamt_Content = "https://media.discordapp.net/attachments/803996377653706752/818772522379640862/unknown.png?width=993&height=1365"

stundenplan = {
    0 : "Heute ist Montag, ihr habt heute\n\n(7:55 Uhr) 1. Stunde: Rat\n(8:40 Uhr) 2. Stunde: Bio\n\n(9:25 - 9:45 Uhr) 1. Pause\n\n(9:45 Uhr) 3. Stunde: Deutsch\n(10:30 Uhr) 4. Stunde: Deutsch\n\n(11:15 - 11:35 Uhr) 2. Pause\n\n(11:35 Uhr) 5. Stunde: Reli/PP\n\n(12:20 - 13:20 Uhr) Mittagspause\n\n(13:20) Uhr 6. Stunde: WP1\n(14:05 Uhr) 7. Stunde: Kunst\n(14:50) Uhr 8. Stunde: Kunst",
    1 : "Heute ist Dienstag, ihr habt also\n\n(7:55 Uhr) 1. Stunde: Mathe\n(8:40 Uhr) 2. Stunde: Mathe\n\n(9:25 - 9:45 Uhr) 1. Pause\n\n(9:45 Uhr) 3. Stunde: Englisch\n(10:30 Uhr) 4. Stunde: Englisch\n\n(11:15 - 11:35 Uhr) 2. Pause\n\n(11:35 Uhr) 5. Stunde: WP1\n(12:20) Uhr 6. Stunde: WP1",
    2 : "Heute ist Dienstag, ne warte heute ist schon Mittwoch, dann habt ihr heute\n\n(7:55 Uhr) 1. Stunde: Englisch\n(8:40 Uhr) 2. Stunde: Englisch\n\n(9:25 - 9:45 Uhr) 1. Pause\n\n(9:45 Uhr) 3. Stunde: GL\n(10:30 Uhr) 4. Stunde: GL\n\n(11:15 - 11:35 Uhr) 2. Pause\n\n(11:35 Uhr) 5. Stunde: AW\n\n(12:20 - 13:20 Uhr) Mittagspause\n\n(13:20 Uhr) 6. Stunde: FöFo/WP2\n(14:05 Uhr) 7. Stunde: Sport\n(14:50 Uhr) 8. Stunde: Sport",
    3 : "Wenn heute Donnerstag ist habt ihr\n\n(7:55 Uhr) 1. Stunde: Mathe\n(8:40 Uhr) 2. Stunde: Mathe\n\n(9:25 - 9:45 Uhr) 1. Pause\n\n(9:45 Uhr) 3. Stunde: Deutsch\n(10:30 Uhr) 4. Stunde: Deutsch\n\n(11:15- 11:35 Uhr) 2. Pause\n\n(11:35 Uhr) 5. Stunde: Reli/PP\n\n(12:20 - 13:20) Mittagspause\n\n(13:20 Uhr) 6. Stunde: Bio\n(14:05 Uhr) 7. Stunde: WP2\n(14:50 Uhr) 8. Stunde: WP2",
    4 : "Die Woche ist fast vorbei, ihr habt heute noch\n\n(7:55 Uhr) 1. Stunde: GL\n(8:40 Uhr) 2. Stunde: GL\n\n(9:25 - 9:45 Uhr) 1. Pause\n\n(9:45 Uhr)  3. Stunde: Chemie\n(10:30 Uhr) 4. Stunde: Chemie\n\n(11:15 - 11:35 Uhr) 2. Pause\n\n(11:35 Uhr) 5. Stunde: AW\n(12:20 Uhr) 6. Stunde: Rat",
    5 : "Sehr witzig, heute ist Samstag, ihr habt Wochenende.",
    6 : "Lasst mich in Ruhe, ich hab Frei."
}

today_stundenplan = stundenplan.get(weekday)