#Aufgabe:   Eine Klasse "Geburtstag" erstellen, die den Geburtstag korrekt ausgeben kann
#Extra:     Monat als Wort ausgeben

#Dictionary um die Monatszahlen mit Wörtern zu ersetzen
monate = {
    1: 'Januar',
    2: 'Februar',
    3: 'März',
    4: 'April',
    5: 'Mai',
    6: 'Juni',
    7: 'Juli',
    8: 'August',
    9: 'September',
    10: 'Oktober',
    11: 'November',
    12: 'Dezember'
}

#Hier wird die Klasse Geburtstag definiert
class Geburtstag:
    #Die __init__ Funktion wird ausgeführt wenn ein Geburtstag Objekt erstellt wird.
    #Die Parameter werden dann angegeben. Bsp: g = Geburtstag(4,7,1999)
    #self wird in jeder Funktion angegeben, da man damit zugriff auf die Variablen der eigenen Klasse (Geburtstag) hat
    def __init__(self, tag, monat, jahr):
        self.tag = tag
        self.monat = monat
        self.jahr = jahr

    #Geburtstag.print()
    #Print Funktion in der die Variablen für den Tag, Monat und Jahr mit Punkten verbunden werden
    def print(self):
        print(str(self.tag) + "." + str(self.monat) + "." + str(self.jahr))

    #print(Geburtstag)
    #Fortgeschrittenere print Funktion, die im Prinzip das gleiche macht wie die vorherige
    def __str__(self):
        return f"{self.tag}.{self.monat}.{self.jahr}"

    #Geburtstag.nicePrint()
    #Die gleiche Funktion wie print(), aber in diesem Fall wird die Zahl von dem monat mit dem entsprechenden Wort ersetzt.

    def nicePrint(self):
        print(str(self.tag) + ". " + str(monate[self.monat]) + " " + str(self.jahr))

geb = Geburtstag(1,11,1999)

print(geb)