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
    for i in range(len(plaintext)):
        symbol = plaintext[i]
        key_symbol = keyword[i % len(keyword)]
        if "A" <= key_symbol <= "Z":
            shift = ord(key_symbol) - ord("A")
        else:
            shift = ord(key_symbol) - ord("a")

        if "A" <= symbol <= "Z":
            number = ord(symbol) - ord("A")
            number = (number + shift) % 26
            ciphertext += chr(number + ord("A"))
        elif "a" <= symbol <= "z":
            number = ord(symbol) - ord("a")
            number = (number + shift) % 26
            ciphertext += chr(number + ord("a"))
        else:
            ciphertext += symbol
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
    for i in range(len(ciphertext)):
        symbol = ciphertext[i]
        key_symbol = keyword[i % len(keyword)]
        if "A" <= key_symbol <= "Z":
            shift = ord(key_symbol) - ord("A")
        else:
            shift = ord(key_symbol) - ord("a")

        if "A" <= symbol <= "Z":
            number = ord(symbol) - ord("A")
            number = (number - shift) % 26  
            plaintext += chr(number + ord("A"))
        elif "a" <= symbol <= "z":
            number = ord(symbol) - ord("a")
            number = (number - shift) % 26
            plaintext += chr(number + ord("a"))
        else:
            plaintext += symbol
    return plaintext