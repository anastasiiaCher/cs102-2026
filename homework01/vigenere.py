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
    i = 0
    keyword_len = len(keyword)

    for char in plaintext:
        if char.isalpha():
            shift_char = keyword[i % keyword_len]
            shift = ord(shift_char.upper()) - ord("A")

            if char.isupper():
                ciphertext += chr((ord(char) - ord("A") + shift) % 26 + ord("A"))
            else:
                ciphertext += chr((ord(char) - ord("a") + shift) % 26 + ord("a"))
        else:
            ciphertext += char
        i += 1
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
    i = 0
    keyword_len = len(keyword)

    for char in ciphertext:
        if char.isalpha():
            shift_char = keyword[i % keyword_len]
            shift = ord(shift_char.upper()) - ord("A")

            if char.isupper():
                plaintext += chr((ord(char) - ord("A") - shift) % 26 + ord("A"))
            else:
                plaintext += chr((ord(char) - ord("a") - shift) % 26 + ord("a"))
        else:
            plaintext += char
        i += 1
    return plaintext
