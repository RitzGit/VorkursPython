# Aufgabe:  n-Gramme erstellen als Liste von Tuples
from typing import List, Tuple, Generator
import re

# Generator
def n_gram(n:int, text: str) -> Generator:
    text_list = re.sub("[!,.]", "", text).split(" ")

    x = 0
    while x+n <= len(text_list):
        yield tuple(text_list[x:x+n])
        x += 1 


text = "Hello there, General Kenobi. You're a bold one to assume that you can simple rickroll a being like me. Only a mere mortal like yours truly would fall for such a cheap trick."
print( list(n_gram(10,text)) )