import random
#^^^^^^^^^^^^ Teil des Extras

#Aufgabe:   Implementiere Mastermind
#Extra:     Zufällig generierte Geheimzahl

#Die Geheimzahl wird in Listenform gespeichert, da dies es einfacher macht die geheimZahl später zugällig zu generieren.
#Die Herangehensweise ist die gleiche wie als wenn es als Text, also String, gespeichert wird, da man die Charaktere in einem String wie eine Liste behandeln kann.
geheimZahl = ['1','2','3','4']

#Extra: Zufällige Geheimzahl
#random.randint generiert eine Zahl zwischen 0-9 zufälligund hängt diese an geheimZahl an.
#Dies passiert 4 mal, also erhalten wir 4 zufällige Stellen.
#geheimZahl = []
#for i in range(4):
#   geheimZahl.append(random.randint(0,9))


while True:
    #Die Zahl des Nutzers wird ausgelesen.
    nutzerZahl = input( "Bitte 4 stellige Zahl eingeben: " )

    #Hier löschen wir jedes Leerzeichen, was sich hereingeschlichen haben könnte. Dies passiert indem wir Leerzeichen mit nichts vertauschen.
    nutzerZahl = nutzerZahl.replace( " ", "" )

    #Hier formen wir die Eingabe direkt in eine Liste um. Bsp: "1357" -> ["1", "3", "5", "7"].
    #Damit ist nutzerZahl von der Form gleich mit der geheimZahl.
    nutzerZahl = list( nutzerZahl )

    #Wie definieren zwei Variablen.
    #Diese Variablen werden bei jedem Rateversuch wieder auf 0 gesetzt.
    #nIndex : Die Anzahl an Zahlen welche an der gleichen Position liegen.
    #nFast  : Die Anzahl an Zahlen die richtig sind, aber nicht an der korrekten Position liegen.
    nIndex = 0
    nFast = 0

    #Hier steigt n von 0 bis 3 auf. range() gibt eine Liste an aufsteigenden natürlichen Zahlen mit 0 zurück. 
    #Die Anzahl der Elemente in dieser Zahlenliste ist die Zahl die in Parametern gegeben wird. 
    #In diesem fall len(nutzerZahl), also die Länge der nutzerZahl, welche 4 ist.
    #Diese Zahlen nutzen wir als Index um auf die nutzerZahl und die geheimeZahl gleichzeitig zuzugreifen.
    for n in range( len( nutzerZahl ) ):

        #Wenn das Element der nutzerZahl an dem Index n dem Element der geheimZahl an n gleich ist, dann sind zwei gleiche Zahlen an der gleichen Position.
        if nutzerZahl[n] == geheimZahl [n]:
            nIndex = nIndex + 1

        #Falls die Zahl an der n-ten Stelle in nutzerZahl nicht gleich der Zahl in geheimZahl an der n-ten Stelle ist,
        #schauen wir ob nutzerZahl[n] an einer anderen Stelle  in der geheimZahl ist.
        #Falls wir nutzerZahl[n] woanders in geheimZahl finden, dann ist diese Zahl richtig, liegt aber an der falschen Position.
        elif nutzerZahl[n] in geheimZahl:
            nFast = nFast + 1

    #Wenn jede Zahl an der richtigen Position ist, dann wurde dir korrekte Zahlenfolge erraten.
    #nIndex wird 4 sein sobald alles richtig erraten wurde. Also kann man davon ausgehen, dass der Spieler gewonnen hat sobald nIndex = 4 ist.
    #Man kann auch davon ausgehen, dass der Spieler noch nicht gewonnen hat solange nIndex nicht 4 ist.
    if nIndex == 4:
        #Falls der Spieler gewonnen hat wird eine Siegesnachricht ausgegeben und break wird genutzt um die while Schleife zu stoppen.
        print("Du hast dir korrekte Zahl erraten!")
        break
    else:
        #Fallss nIndex nicht 4 ist hat der Spieler noch nicht gewonnen und die richtigen Positionen und die richtigen Zahlen werden ausgegeben.
        print("Ziffern an der richtigen Stelle: " + str(nIndex))
        print("Ziffern vorhanden: " + str(nFast))