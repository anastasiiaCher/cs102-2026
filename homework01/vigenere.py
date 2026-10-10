from pydoc import plaintext


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
    while len(keyword) < len(plaintext):
        keyword += keyword
    for i, j in zip(plaintext, keyword):
        if j.isupper():
            shift = ord(j) - 65
        else:
            shift = ord(j) - 97
        if i.isupper():
            ciphertext += chr((ord(i) - 65 + shift) % 26 + 65)
        elif i.islower():
            ciphertext += chr((ord(i) - 97 + shift) % 26 + 97)
        else:
            ciphertext += i
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
    while len(keyword) < len(ciphertext):
        keyword += keyword
    for i, j in zip(ciphertext, keyword):
        if j.isupper():
            shift = ord(j) - 65
        else:
            shift = ord(j) - 97
        if i.isupper():
            plaintext += chr((ord(i) - 65 - shift) % 26 + 65)
        elif i.islower():
            plaintext += chr((ord(i) - 97 - shift) % 26 + 97)
        else:
            plaintext += i
    return plaintext
