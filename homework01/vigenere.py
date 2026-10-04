"""Vigenere cipher."""


def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    key = []
    for i in keyword:
        key.append(ord(i.lower()) - ord("a"))
    b = 0
    for char in plaintext:
        if char.isupper():
            ciphertext += chr((ord(char) - ord("A") + key[b]) % 26 + ord("A"))
        elif char.islower():
            ciphertext += chr((ord(char) - ord("a") + key[b]) % 26 + ord("a"))
        else:
            ciphertext += char
        b += 1
        if b == len(key):
            b = 0
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    key = []
    for i in keyword:
        key.append(ord(i.lower()) - ord("a"))
    b = 0
    for char in ciphertext:
        if char.isupper():
            plaintext += chr((ord(char) - ord("A") - key[b]) % 26 + ord("A"))
        elif char.islower():
            plaintext += chr((ord(char) - ord("a") - key[b]) % 26 + ord("a"))
        else:
            plaintext += char
        b += 1
        if b == len(key):
            b = 0
    return plaintext
