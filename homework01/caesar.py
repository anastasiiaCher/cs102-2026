"""Implementation of the Caesar cipher."""


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """Encrypt plaintext using the Caesar cipher."""
    ciphertext = ""

    for char in plaintext:
        if char.isascii() and char.isupper():
            position = ord(char) - ord("A")
            new_position = (position + shift) % 26
            ciphertext += chr(new_position + ord("A"))

        elif char.isascii() and char.islower():
            position = ord(char) - ord("a")
            new_position = (position + shift) % 26
            ciphertext += chr(new_position + ord("a"))

        else:
            ciphertext += char

    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """Decrypt ciphertext using the Caesar cipher."""
    plaintext = ""

    for char in ciphertext:
        if char.isascii() and char.isupper():
            position = ord(char) - ord("A")
            new_position = (position - shift) % 26
            plaintext += chr(new_position + ord("A"))

        elif char.isascii() and char.islower():
            position = ord(char) - ord("a")
            new_position = (position - shift) % 26
            plaintext += chr(new_position + ord("a"))

        else:
            plaintext += char

    return plaintext
