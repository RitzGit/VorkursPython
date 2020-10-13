#Aufgabe:   Eine Zahlenliste sortieren, wo immer zwei Zahlen nebeneinander verglichen werden
#Extrainfo: Der Algorithmus heißt BubbleSort

#Simple Funktion um zwei Elemente in einer Liste zu tauschen
#Quelle https://www.geeksforgeeks.org/python-program-to-swap-two-elements-in-a-list/
def swap(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1] 
    return list

#Die Funktion zur Sortierung
def bubbleSort(liste):
    #fertig wird als True definiert. Falls zwei Elemente getauscht werden wird dies auf False gesetzt.
    #Wenn nichts getausch wurde, dann bleibt dies auf true, da damit auch die Sortierung fertig ist.
    fertig = True

    for n in range(len(liste)-1):

        #Es wird über die Liste iteriert, aber nur bis zu dem vorletzten Element, 
        #damit kein Problem entsteht, wenn man das letzte mit dem danach vergleichen möchte, welches nicht existiert.
        if liste[n] > liste[n+1]:

            #Falls das erste Element größer ist als das nächste werden diese beiden getauscht und fertig wird auf False gesetzt.
            swap(liste, n, n+1)
            fertig = False
    
    #Sobald fertig zu diesem Punkt True ergibt ist die Sortierung fertig und die fertige Liste wird zurückgegeben.
    if fertig == True:
        return liste
    
    #Falls die Liste noch nicht fertig ist wird die Liste wieder in bubbleSort gegeben um eine neue Iteration zu starten.
    #Das return steht da, damit die endgültige sortierte Liste komplett durchgereicht wird.
    else:
        return bubbleSort(liste)

print(bubbleSort([4,3,7,6,9,3,2]))