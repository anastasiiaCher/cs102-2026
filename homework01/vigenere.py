"""Implementation of the Vigenere cipher."""


def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """Encrypt plaintext using the Vigenere cipher."""
    ciphertext = ""

    for index, char in enumerate(plaintext):
        key_char = keyword[index % len(keyword)]
        shift = ord(key_char.upper()) - ord("A")

        if char.isascii() and char.isupper():
            position = ord(char) - ord("A")
            encrypted_position = (position + shift) % 26
            ciphertext += chr(encrypted_position + ord("A"))

        elif char.isascii() and char.islower():
            position = ord(char) - ord("a")
            encrypted_position = (position + shift) % 26
            ciphertext += chr(encrypted_position + ord("a"))

        else:
            ciphertext += char

    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """Decrypt ciphertext using the Vigenere cipher."""
    plaintext = ""

    for index, char in enumerate(ciphertext):
        key_char = keyword[index % len(keyword)]
        shift = ord(key_char.upper()) - ord("A")

        if char.isascii() and char.isupper():
            position = ord(char) - ord("A")
            decrypted_position = (position - shift) % 26
            plaintext += chr(decrypted_position + ord("A"))

        elif char.isascii() and char.islower():
            position = ord(char) - ord("a")
            decrypted_position = (position - shift) % 26
            plaintext += chr(decrypted_position + ord("a"))

        else:
            plaintext += char

    return plaintext
