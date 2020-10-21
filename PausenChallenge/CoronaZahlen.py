import pandas as pd
import requests

# Holt die neuen Zahlen und speichert diese falls alles funktioniert
res = requests.get('https://stadtplan.bonn.de/csv?OD=4379')
if res.status_code == 200:
    with open('corona.csv', 'w') as file:
        file.write(r.text)

# Liest die corona.csv Datei aus
corona = pd.read_csv('corona.csv',
                    index_col = 'datum',
                    parse_dates=True,
                    sep=';'
)

# Druckt die Felder von corona an denen corona['akut_erkrankt'] größer als 400 ist
print(corona[ corona['akut_erkrankt'] > 400 ] )