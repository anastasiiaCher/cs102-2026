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
        if "A" <= ch <= "Z" or "a" <= ch <= "z":
            shift = ord(keyword[i % len(keyword)].lower()) - ord("a")
            base = ord("A") if ch.isupper() else ord("a")
            ciphertext += chr((ord(ch) - base + shift) % 26 + base)
        else:
            ciphertext += ch
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
        if "A" <= ch <= "Z" or "a" <= ch <= "z":
            shift = ord(keyword[i % len(keyword)].lower()) - ord("a")
            base = ord("A") if ch.isupper() else ord("a")
            plaintext += chr((ord(ch) - base - shift) % 26 + base)
        else:
            plaintext += ch
    return plaintext