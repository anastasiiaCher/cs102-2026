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
    if keyword == "":
        raise ValueError("Keyword must not be empty.")

    for i in range(len(plaintext)):
        char = plaintext[i]
        key_char = keyword[i % len(keyword)].lower()
        shift = ord(key_char) - ord("a")

        if "A" <= char <= "Z":
            first_letter = "A"
        elif "a" <= char <= "z":
            first_letter = "a"
        else:
            # Символ сохраняется, но его позиция учитывается в ключе.
            ciphertext += char
            continue

        position = ord(char) - ord(first_letter)
        new_position = (position + shift) % 26
        ciphertext += chr(ord(first_letter) + new_position)
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
    if keyword == "":
        raise ValueError("Keyword must not be empty.")

    for i in range(len(ciphertext)):
        char = ciphertext[i]
        key_char = keyword[i % len(keyword)].lower()
        shift = ord(key_char) - ord("a")

        if "A" <= char <= "Z":
            first_letter = "A"
        elif "a" <= char <= "z":
            first_letter = "a"
        else:
            plaintext += char
            continue

        position = ord(char) - ord(first_letter)
        new_position = (position - shift) % 26
        plaintext += chr(ord(first_letter) + new_position)
    return plaintext
