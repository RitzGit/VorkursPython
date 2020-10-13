#Aufgabe:   Erstelle einen simplen Taschenrechner mit +,-,*,/
#Extra:     Fehlermeldung bei weiteren Operatoren

while True:
    #Erhält die erste Zahl, zweite Zahl und den Operator als Input und speichert diese ab.
    #int() formt die Zahlen, welche als Text erhalten werden, sofort in Zahlenform um.
    zahl1 = int(input("Erste Zahl"))
    zahl2 = int(input("Zweite Zahl"))
    operator = input("Operator")

    #Schneidet alle Leerzeichen links und rechts von dem Operator ab, falls welche existieren.
    operator = operator.strip()

    #Falls der Operator "+" ist wird sofort das Ergebnis von zahl1 + zahl2 ausgegeben.
    if operator == "+":
        print(zahl1 + zahl2)
    #Falls der Operator "-" ist wird sofort das Ergebnis von zahl1 - zahl2 ausgegeben.
    elif operator == "-":
        print(zahl1 - zahl2)
    #Falls der Operator "*" ist wird sofort das Ergebnis von zahl1 * zahl2 ausgegeben.
    elif operator == "*":
        print(zahl1 * zahl2)
    #Falls der Operator "/" ist wird sofort das Ergebnis von zahl1 / zahl2 ausgegeben.
    elif operator == "/":
        print(zahl1 / zahl2)
    #Falls der Operator auf keine der vorherigen Zeichn zutrifft, dann wird das "else:" Statement betreten.
    #Da der Operator nicht einer der unterstützten Operatoren ist geben wir eine Fehlermeldung zurück.
    else:
        print("Der gegebene Operator ist nicht unterstützt.")
