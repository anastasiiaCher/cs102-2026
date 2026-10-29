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

    key_index = 0

    for char in plaintext:
        if "A" <= char <= "Z":
            base = ord("A")
        elif "a" <= char <= "z":
            base = ord("a")
        else:
            ciphertext += char
            key_index += 1
            continue

        shift = ord(keyword[key_index % len(keyword)].upper()) - ord("A")
        code = ord(char) - base
        new_code = (code + shift) % 26
        ciphertext += chr(new_code + base)
        key_index += 1

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

    key_index = 0

    for char in ciphertext:
        if "A" <= char <= "Z":
            base = ord("A")
        elif "a" <= char <= "z":
            base = ord("a")
        else:
            plaintext += char
            key_index += 1
            continue

        shift = ord(keyword[key_index % len(keyword)].upper()) - ord("A")
        code = ord(char) - base
        new_code = (code - shift) % 26
        plaintext += chr(new_code + base)
        key_index += 1

    return plaintext