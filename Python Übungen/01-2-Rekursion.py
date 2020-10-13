#Aufgabe:   Herausfinden ob eine Zahl gerade oder ungerade ist durch eine Rekursion die immer 2 abzieht

#Die Eingabe wird auf zahl definiert.
zahl = int(input("Eingabe: "))


def testeObGerade(n):
    if n == 0:
        return True
    elif n == -1:
        return False
    n = n-2
    return testeObGerade(n)

#Startet die Funktion und damit die Rekursion mit dem Startwert zahl.
ergebnis = testeObGerade(zahl)

#Ergebnis ist entweder True oder False.
if ergebnis:
    print("Die Zahl ist gerade.")
else:
    print("Die Zahl ist ungerade.")