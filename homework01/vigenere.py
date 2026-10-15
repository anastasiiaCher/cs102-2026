"""pylint is still an annoying brat that requires each and every module to be annotated"""


def encrypt_vigenere(plaintext: str, keyword: str) -> str:"""
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""

    for i, char in enumerate(plaintext):
        if char.islower():
            shift = ord(keyword[i % len(keyword)]) - 97
            ciphertext += chr((ord(char) - 97 + shift) % 26 + 97)
        elif char.isupper():
            shift = ord(keyword[i % len(keyword)]) - 65
            ciphertext += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            ciphertext += char

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

    for i, char in enumerate(ciphertext):
        if char.islower():
            shift = ord(keyword[i % len(keyword)]) - 97
            plaintext += chr((ord(char) - 97 - shift) % 26 + 97)
        elif char.isupper():
            shift = ord(keyword[i % len(keyword)]) - 65
            plaintext += chr((ord(char) - 65 - shift) % 26 + 65)
        else:
            plaintext += char

    return plaintext
