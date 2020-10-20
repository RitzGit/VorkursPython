# Aufgabe:  datetime Objekt erhalten und den letzten Tag des gegebenen Monats ausgeben.
# b):   Werktage in Zeitinterval (Montag-Freitag) ohne Feiertage zählen.

import datetime
import calendar

def last_day_of_month(date):
    return date.replace(day=calendar.monthrange(date.year,date.month)[1])

def count_work_days(start, end):
    date = start
    work_days = 0
    while date < end:
        if date.weekday() < 5:
            work_days += 1
        date += datetime.timedelta(days=1)
    return work_days

list = [datetime.date.today() + datetime.timedelta(days=i) for i in range(0,(datum2 - datum1).days)]

print(list)
