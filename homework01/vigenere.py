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
    for index, symbol in enumerate(plaintext):
        shift = ord(keyword[index % len(keyword)].lower()) - ord("a")
        if "a" <= symbol <= "z":
            start = ord("a")
        elif "A" <= symbol <= "Z":
            start = ord("A")
        else:
            ciphertext += symbol
            continue
        ciphertext += chr(start + (ord(symbol) - start + shift) % 26)
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
    for index, symbol in enumerate(ciphertext):
        shift = ord(keyword[index % len(keyword)].lower()) - ord("a")
        if "a" <= symbol <= "z":
            start = ord("a")
        elif "A" <= symbol <= "Z":
            start = ord("A")
        else:
            plaintext += symbol
            continue
        plaintext += chr(start + (ord(symbol) - start - shift) % 26)
    return plaintext
