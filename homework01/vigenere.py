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
        if "A" <= ch <= "Z":
            ciphertext += chr((ord(ch) - ord("A") + shift) % 26 + ord("A"))
        elif "a" <= ch <= "z":
            ciphertext += chr((ord(ch) - ord("a") + shift) % 26 + ord("a"))
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
        shift = ord(keyword[i % len(keyword)].lower()) - ord("a")
        if "A" <= ch <= "Z":
            plaintext += chr((ord(ch) - ord("A") - shift) % 26 + ord("A"))
        elif "a" <= ch <= "z":
            plaintext += chr((ord(ch) - ord("a") - shift) % 26 + ord("a"))
        else:
            plaintext += ch
    return plaintext
