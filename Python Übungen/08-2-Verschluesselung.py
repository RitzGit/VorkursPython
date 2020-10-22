# Aufgabe:  Caesar Verschlüsselung
import re


def move_letter(char: str, key: int) -> chr:
    char = char.lower()

    if key < 0:
        while key < 0:
            key += 26

    if ord(char) + key <= 122:
        return(chr(ord(char) + key))
    else:
        num = ord(char) + key
        while num > 122:
            num -= 26
        return(chr(num))

def encode_caesar_cipher(input: str, key: int) -> str:
    input = input.lower()

    output = ''
    for char in input:
        if re.match('[a-z]', char) is not None:
            output += move_letter(char, key)
        else:
            output += char
    return output

def decode_caesar_cipher(input: str, key: str) -> str:
    input = input.lower()
    output = encode_caesar_cipher(input, key * (-1))
    return output

print(decode_caesar_cipher('SNXG VFG, QNFF NYYRF VZ HAVIREFHZ RAGJRQRE RVAR XNEGBSSRY VFG BQRE AVPUG', 13))