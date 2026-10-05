"""Vigenere cipher."""

import string


def _shift_char(ch: str, shift: int) -> str:
    """Shifts a single Latin letter by the given amount, keeping its case."""
    if ch not in string.ascii_letters:
        return ch
    base = ord("A") if ch.isupper() else ord("a")
    return chr((ord(ch) - base + shift) % 26 + base)


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
    for i, ch in enumerate(plaintext):
        shift = ord(keyword[i % len(keyword)].lower()) - ord("a")
        ciphertext += _shift_char(ch, shift)
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
    for i, ch in enumerate(ciphertext):
        shift = ord(keyword[i % len(keyword)].lower()) - ord("a")
        plaintext += _shift_char(ch, -shift)
    return plaintext
