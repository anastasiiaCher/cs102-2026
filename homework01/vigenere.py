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
    for i, char in enumerate(plaintext):
        key_char = keyword[i % len(keyword)]
        shift = ord(key_char.upper()) - ord("A")
        if "A" <= char <= "Z":
            base = ord("A")
            ciphertext += chr((ord(char) - base + shift) % 26 + base)
        elif "a" <= char <= "z":
            base = ord("a")
            ciphertext += chr((ord(char) - base + shift) % 26 + base)
        else:
            ciphertext += char
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
    for i, char in enumerate(ciphertext):
        key_char = keyword[i % len(keyword)]
        shift = ord(key_char.upper()) - ord("A")
        if "A" <= char <= "Z":
            base = ord("A")
            plaintext += chr((ord(char) - base - shift) % 26 + base)
        elif "a" <= char <= "z":
            base = ord("a")
            plaintext += chr((ord(char) - base - shift) % 26 + base)
        else:
            plaintext += char
    return plaintext
