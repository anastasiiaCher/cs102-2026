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
        if char.isupper():
            shift = ord(keyword[key_index % len(keyword)].upper()) - ord('A')
            new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            ciphertext += new_char
        elif char.islower():
            shift = ord(keyword[key_index % len(keyword)].upper()) - ord('A')
            new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            ciphertext += new_char
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
        if char.isupper():
            shift = ord(keyword[key_index % len(keyword)].upper()) - ord('A')
            new_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            plaintext += new_char
        elif char.islower():
            shift = ord(keyword[key_index % len(keyword)].upper()) - ord('A')
            new_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            plaintext += new_char
        else:
            plaintext += char
        key_index += 1

    return plaintext