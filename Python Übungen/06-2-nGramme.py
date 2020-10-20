# Aufgabe:  n-Gramme erstellen als Liste von Tuples
from typing import List, Tuple
# Generator
def n_gram(n:int, text: str) -> List[Tuple[str,...]]:
    text_list = text.replace("!", "").replace(",","").replace(".","").split(" ")

    x = 0
    while x+n <= len(text_list):
        yield tuple(text_list[x:x+n])
        x += 1 

for a in n_gram(2, "1 2 3 4 5 6"):
    print(a)