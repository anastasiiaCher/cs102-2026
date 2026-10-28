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
    for index, i in enumerate(plaintext):
        key_index = index % len(keyword)
        key_letter = keyword[key_index]
        if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            shift = ord(key_letter.upper()) - ord("A")
            position = ord(i) - ord("A")
            new_position = (position + shift) % 26
            ciphertext += chr(new_position + ord("A"))
        elif i in "abcdefghijklmnopqrstuvwxyz":
            shift = ord(key_letter.upper()) - ord("A")
            position = ord(i) - ord("a")
            new_position = (position + shift) % 26
            ciphertext += chr(new_position + ord("a"))
        else:
            ciphertext += i
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
    for index, i in enumerate(ciphertext):
        key_index = index % len(keyword)
        key_letter = keyword[key_index]
        if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            shift = ord(key_letter.upper()) - ord("A")
            position = ord(i) - ord("A")
            new_position = (position - shift) % 26
            plaintext += chr(new_position + ord("A"))
        elif i in "abcdefghijklmnopqrstuvwxyz":
            shift = ord(key_letter.upper()) - ord("A")
            position = ord(i) - ord("a")
            new_position = (position - shift) % 26
            plaintext += chr(new_position + ord("a"))
        else:
            plaintext += i
    return plaintext
