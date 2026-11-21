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
    key = keyword.upper()
    index = 0

    for char in plaintext:
        if "A" <= char <= "Z":
            shift = ord(key[index % len(key)]) - 65
            ciphertext += chr((ord(char) - 65 + shift) % 26 + 65)
            index += 1

        elif "a" <= char <= "z":
            shift = ord(key[index % len(key)]) - 65
            ciphertext += chr((ord(char) - 97 + shift) % 26 + 97)
            index += 1

        else:
            ciphertext += char
            index += 1

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
    key = keyword.upper()
    index = 0

    for char in ciphertext:
        if "A" <= char <= "Z":
            shift = ord(key[index % len(key)]) - 65
            plaintext += chr((ord(char) - 65 - shift) % 26 + 65)
            index += 1

        elif "a" <= char <= "z":
            shift = ord(key[index % len(key)]) - 65
            plaintext += chr((ord(char) - 97 - shift) % 26 + 97)
            index += 1

        else:
            plaintext += char
            index += 1

    return plaintext
