#Aufgabe:   Herausfinden ob eine Zahl gerade oder ungerade ist durch eine Rekursion die immer 2 abzieht

#Die Eingabe wird auf zahl definiert.
zahl = int(input("Eingabe: "))


def testeObGerade(n):
    n = n-2
    if n == 0:
        return True
    elif n == -1:
        return False
    return testeObGerade(n)

#Startet die Funktion und damit die Rekursion mit dem Startwert zahl.
testeObGerade(zahl)