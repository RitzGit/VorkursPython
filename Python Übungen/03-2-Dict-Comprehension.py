# Aufgabe:   Häufigkeit jedes Buchstaben in dem Lorem Ipsum Text als Dictionary ausgeben.
import time

text = """Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam
nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo
duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet."""

# Jeder Buchstabe wird klein gemacht um das zählen zu vereinfachen.
text = text.lower()

# text.count() gibt die Anzahl eines Buchstaben wieder.
# Wir zählen also bei jedem Buchstaben die ANzahl und speichern sie unter dem Buchstaben als Schlüssel.
# ord(buchstabe) >= 97 and ord(buchstabe) <= 122 konvertiertden buchstaben jeweils in eine Zahl, die wir mit der ASCII Tabelle vergleichen können.
# Damit wird getestet ob der Buchstabe auf dieser Tabelle zwischen a und z liegt.
buchstaben_zaehler = {buchstabe: text.count(buchstabe) for buchstabe in text if (ord(buchstabe) >= 97 and ord(buchstabe) <= 122)}

# Kürzer, aber komplizierter.
mega_zaehler = {char: text.count(char) for char in set(text) if (97 <= ord(char) <= 122)}
