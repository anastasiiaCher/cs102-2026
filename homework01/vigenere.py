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
    key_shifts = [ord(ch.lower()) - ord("a") for ch in keyword]
    
    for i, ch in enumerate(plaintext):
        shift = key_shifts[i % len(key_shifts)]
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
    if not keyword:
        return ciphertext
    key_shifts = [ord(ch.lower()) - ord("a") for ch in keyword]
    
    for i, ch in enumerate(ciphertext):
        shift = key_shifts[i % len(key_shifts)]
        if "A" <= ch <= "Z":
            plaintext += chr((ord(ch) - ord("A") - shift) % 26 + ord("A"))
        elif "a" <= ch <= "z":
            plaintext += chr((ord(ch) - ord("a") - shift) % 26 + ord("a"))
        else:
            plaintext += ch
    return plaintext