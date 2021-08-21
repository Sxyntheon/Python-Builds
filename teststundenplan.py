class Stundenplan:
    def __init__(self, weekday_name, weekday_count, weekday_content):
        self.name = weekday_name
        self.weekday = weekday_count
        self.content = weekday_content

Monday = Stundenplan("Monday", 1, "Heute ist Montag, ihr habt heute\n\n(7:55 Uhr) 1. Stunde: Rat\n(8:40 Uhr) 2. Stunde: Bio\n\n(9:25 - 9:45 Uhr) 1. Pause\n\n(9:45 Uhr) 3. Stunde: Deutsch\n(10:30 Uhr) 4. Stunde: Deutsch\n\n(11:15 - 11:35 Uhr) 2. Pause\n\n(11:35 Uhr) 5. Stunde: Reli/PP\n\n(12:20 - 13:20 Uhr) Mittagspause\n\n(13:20) Uhr 6. Stunde: WP1\n(14:05 Uhr) 7. Stunde: Kunst\n(14:50) Uhr 8. Stunde: Kunst")
print(Monday.content)
