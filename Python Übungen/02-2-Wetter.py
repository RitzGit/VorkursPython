#Aufgabe:   Die API von wttr.in ansprechen mit einer Klasse namens StadtWetter.
import requests
import json

#Die Klasse StadtWetter wird erstellt.
class StadtWetter:
    #In dem Konstruktor wird erst die Stadt abgespeichert und dann werden die Wetterdaten mit self.grabData() abgespeichert.
    def __init__(self, stadt):
        self.stadt = stadt.lower()
        self.data = self.grabData()

    #grabData() macht eine Request an wttr.in mit der Stadt und gibt es in Form einer json Datei aus.
    def grabData(self):
        r = requests.get(f'https://wttr.in/{self.stadt}?format=j1')
        return r.json()

    #Unter self.data['current_codition'][0] wird die jetzige Wettersituation gespeichert.
    def wetterJetzt(self):
        w = self.data['current_condition'][0]

        #Die verschiedenen Daten die wir wollen werden dann in eine Rückmeldung angehangen.
        #\n gibt einen Zeilenumbruch an, damit es lesbarer ist.
        response = "Die jetzige Wetterlage\n\n"
        response += f"Wetter: {w['weatherDesc'][0]['value']}\n"
        response += f"Temperatur: {w['temp_C']}°C\n"
        response += f"Gefühlt: {w['FeelsLikeC']}°C\n"
        response += f"Luftfeuchtigkeit: {w['humidity']}%\n"
        response += f"Wind: {w['windspeedKmph']} km/h\n"

        return response

    #temp gibt die Temperaturdaten für den ganzen heutigen Tag. Diese sind unter self.data['weather'][0] gespeichert.
    def temp(self):
        w = self.data['weather'][0]

        response = "Die heutige Temperatur\n\n"
        response += f"Temperatur: {w['mintempC']} - {w['maxtempC']}°C\n"

        return response

    #temp gibt die Temperaturdaten für den ganzen morgigen Tag. Diese sind unter self.data['weather'][1] gespeichert.
    def tempMorgen(self):
        w = self.data['weather'][1]

        response = "Die morgige Temperatur\n\n"
        response += f"Temperatur: {w['mintempC']} - {w['maxtempC']}°C\n"

        return response

#Die StadtWetter Klasse wird erstellt und die verschiedenen Funktionen werden ausgeführt.
wetter = StadtWetter('Bonn')
print(wetter.wetterJetzt())
print(wetter.temp())
print(wetter.tempMorgen())