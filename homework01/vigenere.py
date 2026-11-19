"""Модуль шифрования и расшифрования шифром Виженера."""


def _shift_value(key_char: str) -> int:
    """Возвращает величину сдвига для символа ключа."""
    if "A" <= key_char <= "Z":
        return ord(key_char) - ord("A")
    if "a" <= key_char <= "z":
        return ord(key_char) - ord("a")
    return 0


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
    if not keyword:
        return plaintext

    key_idx = 0
    key_len = len(keyword)
    for char in plaintext:
        shift = _shift_value(keyword[key_idx % key_len])
        if "A" <= char <= "Z":
            base = ord("A")
            ciphertext += chr(base + (ord(char) - base + shift) % 26)
        elif "a" <= char <= "z":
            base = ord("a")
            ciphertext += chr(base + (ord(char) - base + shift) % 26)
        else:
            ciphertext += char
        key_idx += 1
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
    if not keyword:
        return ciphertext

    key_idx = 0
    key_len = len(keyword)
    for char in ciphertext:
        shift = _shift_value(keyword[key_idx % key_len])
        if "A" <= char <= "Z":
            base = ord("A")
            plaintext += chr(base + (ord(char) - base - shift) % 26)
        elif "a" <= char <= "z":
            base = ord("a")
            plaintext += chr(base + (ord(char) - base - shift) % 26)
        else:
            plaintext += char
        key_idx += 1
    return plaintext
