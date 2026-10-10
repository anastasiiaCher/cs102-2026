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
    for x in plaintext:
        first_sym = key.lower()[0]
        key = key[1:]
        if x not in "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm":
            ciphertext += x
        else:
            shift = ord(first_sym) - 97
            if x.islower() == 1:
                if ord(x) + shift > 122:
                    ciphertext += chr(ord(x) + shift - 26)
                else:
                    ciphertext += chr(ord(x) + shift)
            else:
                if ord(x) + shift > 90:
                    ciphertext += chr(ord(x) + shift - 26)
                else:
                    ciphertext += chr(ord(x) + shift)
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
    for x in ciphertext:
        first_sym = key.lower()[0]
        key = key[1:]
        if x not in "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm":
            plaintext += x
        else:
            shift = ord(first_sym) - 97
            if x.islower() == 1:
                if ord(x) - shift >= 97:
                    plaintext += chr(ord(x) - shift)
                else:
                    plaintext += chr(ord(x) - shift + 26)
            else:
                if ord(x) - shift >= 65:
                    plaintext += chr(ord(x) - shift)
                else:
                    plaintext += chr(ord(x) - shift + 26)
    return plaintext
