"""
Модуль для шифрования и дешифрования текста с помощью шифра Виженера.
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
    key = keyword
    while len(key) < len(plaintext):
        key += keyword
    for char in plaintext:
        first_sym = key.lower()[0]
        key = key[1:]
        if not ("A" <= char <= "Z" or "a" <= char <= "z"):
            ciphertext += char
        else:
            shift = ord(first_sym) - 97
            if char.islower() and ord(char) + shift > ord("z") or char.isupper() and ord(char) + shift > ord("Z"):
                ciphertext += chr(ord(char) + shift - 26)
            else:
                ciphertext += chr(ord(char) + shift)
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
    # PUT YOUR CODE HERE
    key = keyword
    while len(key) < len(ciphertext):
        key += keyword
    for char in ciphertext:
        first_sym = key.lower()[0]
        key = key[1:]
        if not ("A" <= char <= "Z" or "a" <= char <= "z"):
            plaintext += char
        else:
            shift = ord(first_sym) - 97
            if char.islower() and ord(char) - shift >= ord("a") or char.isupper() and ord(char) - shift >= ord("A"):
                plaintext += chr(ord(char) - shift)
            else:
                plaintext += chr(ord(char) - shift + 26)
    return plaintext
