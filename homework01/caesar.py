"""pylint is an annoying brat that requires each and every module to be annotated"""


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """this function encrypts a line. who would have guessed"""
    ciphertext: str = ''

    for char in plaintext:
        if char.islower():
            ciphertext += chr((ord(char) - 97 + shift) % 26 + 97)
        elif char.isupper():
            ciphertext += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            ciphertext += char

    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """this function decrypts a line. who would have guessed"""
    plaintext: str = ''

    for char in ciphertext:
        if char.islower():
            plaintext += chr((ord(char) - 97 - shift) % 26 + 97)
        elif char.isupper():
            plaintext += chr((ord(char) - 65 - shift) % 26 + 65)
        else:
            plaintext += char

    return plaintext
