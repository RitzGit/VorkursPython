# Aufgabe:  Morsecode encoding und decoding

import re

morse = {
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p': '.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..',
    ' ': ''
}

def morse_encode(input: str) -> str:
    input = input.lower()
    input = re.sub('[^a-z ]','',input)

    output = ''
    for char in input:
        output += morse[char] + ' '

    return output

def morse_decode(input: str) -> str:
    reverse_morse = {value : key for key, value in morse.items()}
    reverse_morse[''] = ' '
    input = input.split(' ')

    output = ''
    for char in input:
        output += reverse_morse[char]
    return output

print(morse_encode('test test'))
print(morse_decode('- . ... -  - . ... -'))

print(morse_decode('.- .-.. .-..  -.-- --- ..- .-.  -... .- ... .  .- .-. .  -... . .-.. --- -. --.  - ---  ..- ...'))