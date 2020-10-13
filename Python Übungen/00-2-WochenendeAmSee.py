#Aufgabe:   Füge die Einkaufslisten zusammen und gib sie wieder als ein Dictionary.
#Extra:     Gut lesbare Ausgabe.

alice = ['Bananen', 'Brot', 'Schokolade', 'Rotwein']
bob = ['Bier', 'Bier', 'Chips']
eve = ['Brot', 'Schokolade', 'Chips', 'Bier', 'Wasser']

#Fügt alle dre Listen zu einer zusammen in der alle Element enthalten sind
gesamteListe = alice+bob+eve
einkaufsliste = {}

#Läuft durch jedes Element von der gesamten Liste durch
for element in gesamteListe:

    #einkaufsliste.keys() gibt eine Liste mit allen Elementen die in dem Dictionary Einkaufsliste enthalten sind zurück.
    #Falls unser Element sich in der Einkaufsliste bereits befindet, dann muss es bereits einen Zahlenwert haben, welchen wir dann um 1 erhöhen
    if element in einkaufsliste.keys():
        einkaufsliste[element] = einkaufsliste[element] + 1
    
    #Falls sich unser Element nicht in der Einkaufsliste befindet, dann setzen wir die Menge in der Einkaufsliste auf 1
    else:
        einkaufsliste[element] = 1

#Extra: Lesbare Ausgabe
#Wir lesen wieder jedes Element der Eunkaufsliste aus
#Dann drucken wir das Element neben dem Wert des Elementen im Dictionary, also neben der totalen Anzahl auf allen Einkaufslisten.
for e in einkaufsliste.keys():
    print(e + " : " + str(einkaufsliste[e]))