"""pylint is still an annoying brat that requires each and every module to be annotated"""


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

    len_alphabet = len("abcdefghijklmnopqrstuvwxyz")

    for i, char in enumerate(plaintext):
        if char.islower():
            shift = ord(keyword[i % len(keyword)]) - ord("a")
            ciphertext += chr((ord(char) - ord("a") + shift) % len_alphabet + ord("a"))
        elif char.isupper():
            shift = ord(keyword[i % len(keyword)]) - ord("A")
            ciphertext += chr((ord(char) - ord("A") + shift) % len_alphabet + ord("A"))
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

    len_alphabet = len("abcdefghijklmnopqrstuvwxyz")

    for i, char in enumerate(ciphertext):
        if char.islower():
            shift = ord(keyword[i % len(keyword)]) - ord("a")
            plaintext += chr((ord(char) - ord("a") - shift) % len_alphabet + ord("a"))
        elif char.isupper():
            shift = ord(keyword[i % len(keyword)]) - ord("A")
            plaintext += chr((ord(char) - ord("A") - shift) % len_alphabet + ord("A"))
        else:
            plaintext += char

    return plaintext
