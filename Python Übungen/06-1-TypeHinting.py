# Aufgabe:  Erweitern durch Typehinting
from typing import List, Set, Dict, Tuple, Optional
def flaecheninhalt ( breite: int , laenge: int ) -> int:
    return breite * laenge

def zeichenzaehlen ( text: str ) -> Dict[str, str]:
    return { character : text . count ( character ) for character in text }

def fancy_function ( namen_und_matrikelnummern: List[Tuple[str,int]] ,
                    semester: int ,
                    bestanden: Optional[bool] = False ):
    for eintrag in namen_und_matrikelnummern :
        print ( f'Student { eintrag [0]} ({ eintrag [1]}) ')
        print ( f'Im { semester }. Semester hat ')
        print ( f'{" nicht " if not bestanden else ""} bestanden .')