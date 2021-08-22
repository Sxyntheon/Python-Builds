from datetime import date

today = date.today()

weekday = today.weekday()

Stundenplan_Gesamt_Content = "Nicht verfügbar"

stundenplan = {
    0 : "Heute ist Montag, ihr habt heute\n\n(7:55 Uhr) 1. Stunde: Rat\n(8:40 Uhr) 2. Stunde: PP/Reli\n\n(9:25 - 9:45 Uhr) 1. Pause\n\n(9:45 Uhr) 3. Stunde: Chemie\n(10:30 Uhr) 4. Stunde: Chemie\n\n(11:15 - 11:35 Uhr) 2. Pause\n\n(11:35 Uhr) 5. Stunde: Musik\n\n(12:20 - 13:20 Uhr) Mittagspause\n\n(13:20) Uhr 6. Stunde: LBZ\n(14:05 Uhr) 7. Stunde: Physik\n(14:50) Uhr 8. Stunde: Physik",
    1 : "Heute ist Dienstag, ihr habt also\n\n(7:55 Uhr) 1. Stunde: WP1\n(8:40 Uhr) 2. Stunde: WP1\n\n(9:25 - 9:45 Uhr) 1. Pause\n\n(9:45 Uhr) 3. Stunde: Mathe\n(10:30 Uhr) 4. Stunde: Mathe\n\n(11:15 - 11:35 Uhr) 2. Pause\n\n(11:35 Uhr) 5. Stunde: Englisch\n(12:20) Uhr 6. Stunde: Englisch",
    2 : "Heute ist Dienstag, ne warte heute ist schon Mittwoch, dann habt ihr heute\n\n(7:55 Uhr) 1. Stunde: Deutsch\n(8:40 Uhr) 2. Stunde: Deutsch\n\n(9:25 - 9:45 Uhr) 1. Pause\n\n(9:45 Uhr) 3. Stunde: AT/AH\n(10:30 Uhr) 4. Stunde: AT/AH\n\n(11:15 - 11:35 Uhr) 2. Pause\n\n(11:35 Uhr) 5. Stunde: PP/Reli\n\n(12:20 - 13:20 Uhr) Mittagspause\n\n(13:20 Uhr) 6. Stunde: FöFo/Latein\n(14:05 Uhr) 7. Stunde: GL\n(14:50 Uhr) 8. Stunde: GL",
    3 : "Wenn heute Donnerstag ist habt ihr\n\n(7:55 Uhr) 1. Stunde: Englisch\n(8:40 Uhr) 2. Stunde: Englisch\n\n(9:25 - 9:45 Uhr) 1. Pause\n\n(9:45 Uhr) 3. Stunde: Deutsch\n(10:30 Uhr) 4. Stunde: Deutsch\n\n(11:15- 11:35 Uhr) 2. Pause\n\n(11:35 Uhr) 5. Stunde: WP1\n\n(12:20 - 13:20) Mittagspause\n\n(13:20 Uhr) 6. Stunde: FöFo/Latein\n(14:05 Uhr) 7. Stunde: Sport\n(14:50 Uhr) 8. Stunde: Latein",
    4 : "Die Woche ist fast vorbei, ihr habt heute noch\n\n(7:55 Uhr) 1. Stunde: LBZ\n(8:40 Uhr) 2. Stunde: FöFo/Latein\n\n(9:25 - 9:45 Uhr) 1. Pause\n\n(9:45 Uhr)  3. Stunde: Mathe\n(10:30 Uhr) 4. Stunde: Mathe\n\n(11:15 - 11:35 Uhr) 2. Pause\n\n(11:35 Uhr) 5. Stunde: Musik\n(12:20 Uhr) 6. Stunde: Rat",
    5 : "Sehr witzig, heute ist Samstag, ihr habt Wochenende.",
    6 : "Lasst mich in Ruhe, ich hab Frei."
}

today_stundenplan = stundenplan.get(weekday)