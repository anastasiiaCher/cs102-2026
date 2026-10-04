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
    key = []
    for i in keyword:
        if i.isupper():
            key.append((ord(i) - ord('A')) % 26 + ord('A'))
        elif i.islower():
            key.append((ord(i) - ord('a')) % 26 + ord('a'))
    b = 0
    for a in range(len(plaintext)):
        if key[b] == ord("A") or key[b] == ord("a"):
            ciphertext += plaintext[a]
        elif plaintext[a].isupper():
            ciphertext += chr((ord(plaintext[a]) + key[b]) % 26 + ord('A'))
        elif plaintext[a].islower():
            ciphertext += chr((ord(plaintext[a]) + key[b]) % 26 + ord('a'))
        b += 1
        if b == len(key):
            b = 0
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
    key = []
    for i in keyword:
        if i.isupper():
            key.append((ord(i) - ord('A')) % 26 + ord('A'))
        elif i.islower():
            key.append((ord(i) - ord('a')) % 26 + ord('a'))
    b = 0
    for a in range(len(ciphertext)):
        if key[b] == ord("A") or key[b] == ord("a"):
            plaintext += ciphertext[a]
        elif ciphertext[a].isupper():
            plaintext += chr((ord(ciphertext[a]) - key[b]) % 26 + ord('A'))
        elif ciphertext[a].islower():
            plaintext += chr((ord(ciphertext[a]) - key[b]) % 26 + ord('a'))
        b += 1
        if b == len(key):
            b = 0
    return plaintext