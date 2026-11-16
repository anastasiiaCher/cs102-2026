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
    key = keyword * (len(plaintext) // len(keyword)) + keyword[: len(plaintext) % len(keyword)]
    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            if plaintext[i].isupper():
                key_upd = key[i].upper()
                shift_start = ord("A")
                shift = ord(key_upd) - shift_start
                encrypted_symbol = chr((ord(plaintext[i]) - shift_start + shift) % 26 + shift_start)
                ciphertext += encrypted_symbol
            else:
                key_upd = key[i].lower()
                shift_start = ord("a")
                shift = ord(key_upd) - shift_start
                encrypted_symbol = chr((ord(plaintext[i]) - shift_start + shift) % 26 + shift_start)
                ciphertext += encrypted_symbol
        else:
            ciphertext += plaintext[i]
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
    key = keyword * (len(ciphertext) // len(keyword)) + keyword[: len(ciphertext) % len(keyword)]
    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            if ciphertext[i].isupper():
                key_upd = key[i].upper()
                shift_start = ord("A")
                shift = ord(key_upd) - shift_start
                decrypted_symbol = chr((ord(ciphertext[i]) - shift_start - shift) % 26 + shift_start)
                plaintext += decrypted_symbol
            else:
                key_upd = key[i].lower()
                shift_start = ord("a")
                shift = ord(key_upd) - shift_start
                decrypted_symbol = chr((ord(ciphertext[i]) - shift_start - shift) % 26 + shift_start)
                plaintext += decrypted_symbol
        else:
            plaintext += ciphertext[i]
    return plaintext
