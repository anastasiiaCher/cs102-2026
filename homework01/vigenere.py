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
        if char.isalpha():
            key_char = keyword[key_index % len(keyword)]

            if key_char.isupper():
                shift = ord(key_char) - ord("A")
            else:
                shift = ord(key_char) - ord("a")

            if char.isupper():
                base = ord("A")
                ciphertext += chr((ord(char) - base + shift) % 26 + base)
            else:
                base = ord("a")
                ciphertext += chr((ord(char) - base + shift) % 26 + base)
        else:
            ciphertext += char

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
        if char.isalpha():
            key_char = keyword[key_index % len(keyword)]

            if key_char.isupper():
                shift = ord(key_char) - ord("A")
            else:
                shift = ord(key_char) - ord("a")

            if char.isupper():
                base = ord("A")
                plaintext += chr((ord(char) - base - shift) % 26 + base)
            else:
                base = ord("a")
                plaintext += chr((ord(char) - base - shift) % 26 + base)
        else:
            plaintext += char

        key_index += 1

    return plaintext
