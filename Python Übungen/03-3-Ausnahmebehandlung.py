# Aufgabe:   Textschnipsel von Pastebinn herunterladen mit response und Fehlre abfangen.
# Schnipsel-IDs: LIaSudG3, pmZ2Q0gU, AeUNgdAb
import json

import requests


def grab_schnipsel(id):
    url = f"https://pastebin.com/raw/{id}"
    res = requests.get(url)

    try:
        res.raise_for_status()
        response = res.json()
        result = ""
        for key in response.keys():
            result += response[key] + " "
        return result.strip()
    except requests.exceptions.HTTPError:
        pass
    except json.decoder.JSONDecodeError:
       return res.text


print(grab_schnipsel("LIaSudG3"))
print(grab_schnipsel("pmZ2Q0gU"))
print(grab_schnipsel("AeUNgdAb"))