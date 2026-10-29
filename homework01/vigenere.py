"""функции для кодирования и декодирования шифра Виженере"""


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
    keyword = (keyword * (len(plaintext) // len(keyword) + 1))[: len(plaintext)].lower()
    for a, b in zip(plaintext, keyword.lower()):
        base = ord("A") if a.isupper() else ord("a")
        shift = ord(b) - ord("a")
        if a.isalpha():
            ciphertext += chr(base + (ord(a) - base + shift) % 26)
        else:
            ciphertext += a

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
    keyword = (keyword * (len(ciphertext) // len(keyword) + 1))[: len(ciphertext)].lower()
    for a, b in zip(ciphertext, keyword.lower()):
        base = ord("A") if a.isupper() else ord("a")
        shift = ord(b) - ord("a")
        if a.isalpha():
            plaintext += chr(base + (ord(a) - base - shift) % 26)
        else:
            plaintext += a
    return plaintext
