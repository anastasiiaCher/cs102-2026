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
    shifts = [ord(letter.lower()) - ord("a") for letter in keyword]
    for i, char in enumerate(plaintext):
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            ciphertext += chr((ord(char) - base + shifts[i % len(shifts)]) % 26 + base)
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
    shifts = [ord(letter.lower()) - ord("a") for letter in keyword]
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            plaintext += chr((ord(char) - base - shifts[i % len(shifts)]) % 26 + base)
        else:
            plaintext += char
    return plaintext
