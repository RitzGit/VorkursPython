#Aufgabe:   Die Bonner Covid Daten auswerten mit requests und csv Dateien
#API    Link:   https://stadtplan.bonn.de/csv?OD=4379
import requests
import csv
from datetime import datetime

#r = requests.get("https://stadtplan.bonn.de/csv?OD=4379")
#f = open("covid19-data.csv", "w")
#f.write(r.text)
#f.close()

#Liest die Daten aus der Datei aus.
def getData():
    with open("covid19-data.csv") as csvdatei:
        csvinhalt = csv.DictReader(csvdatei, delimiter=';')
        csvlist = list(csvinhalt)

        #Alle leeren Felder in den Daten werden mit '0' ersetzt im später Probleme zu vermeiden
        for i in csvlist:
            for k in i.keys():
                if i[k] == '':
                    i[k] = '0'

        return csvlist

#Die Daten werden nach dem Datum sortiert
def sortData(data):
    #datetime.strptime(a['datum'], '%Y-%m-%d').timestamp() formt alle Datums in den Daten in Sekunden um,
    #damit diese Sekunden als Sortierungsschlüssel benutzt werden können.
    return sorted(data, key= lambda a: datetime.strptime(a['datum'], '%Y-%m-%d').timestamp())

#Alle Tage an denen die akut erkrankten über mind sind
def akut(data, mind):
    #Die filter() Funktion nimmt eine Liste und einen key. In diesem Fall ist der key |lambda a: int(a['akut_erkrankt']) > mind|.
    #Dieser gibt aus ob die akut erkrankten über dem Mindestwert sind und gibt dann alle als Liste aus, auf die das zutrifft.
    return list(filter(lambda a: int(a['akut_erkrankt']) > mind, data))

#Der Tag an dem es die meisten neuen positiven Fälle gab.
def mostPositive(data):
    #In diesem Fall sortieren wir nach der Menge an den positiv getesteten Personen und geben dann das letzte ELement zurück.
    return sorted(data, key= lambda a: int(a['positiv_getest']))[-1]

data = getData()
print(sortData(data)[0])
print(mostPositive(data))