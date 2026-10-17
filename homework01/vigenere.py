"""
Module containing Vigenere cipher encryption and decryption functions.
"""


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
    keyword = keyword.upper()
    keyword_index = 0
    for letter in plaintext:
        if letter.isupper():
            ciphertext += chr(
                ((ord(letter) - ord("A")) + (ord(keyword[keyword_index % len(keyword)]) - ord("A"))) % 26 + ord("A")
            )
        elif letter.islower():
            ciphertext += chr(
                ((ord(letter) - ord("a")) + (ord(keyword[keyword_index % len(keyword)]) - ord("A"))) % 26 + ord("a")
            )
        else:
            ciphertext += letter
        keyword_index += 1
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
    keyword = keyword.upper()
    keyword_index = 0
    for letter in ciphertext:
        if letter.isupper():
            plaintext += chr(
                ((ord(letter) - ord("A")) - (ord(keyword[keyword_index % len(keyword)]) - ord("A"))) % 26 + ord("A")
            )
        elif letter.islower():
            plaintext += chr(
                ((ord(letter) - ord("a")) - (ord(keyword[keyword_index % len(keyword)]) - ord("A"))) % 26 + ord("a")
            )
        else:
            plaintext += letter
        keyword_index += 1
    return plaintext
