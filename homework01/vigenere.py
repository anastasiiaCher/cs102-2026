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
    if not keyword.isascii() or not keyword.isalpha():
        raise ValueError("keyword must contain only English letters")

    keyword = keyword.upper()
    key_index = 0

    for char in plaintext:
        if "A" <= char <= "Z":
            base = ord("A")
        elif "a" <= char <= "z":
            base = ord("a")
        else:
            ciphertext += char
            continue

        key_letter = keyword[key_index % len(keyword)]
        shift = ord(key_letter) - ord("A")
        ciphertext += chr(base + (ord(char) - base + shift) % 26)
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
    if not keyword.isascii() or not keyword.isalpha():
        raise ValueError("keyword must contain only English letters")

    inverse_keyword = ""
    for letter in keyword.upper():
        shift = ord(letter) - ord("A")
        inverse_keyword += chr(ord("A") + (-shift) % 26)

    plaintext = encrypt_vigenere(ciphertext, inverse_keyword)
    return plaintext