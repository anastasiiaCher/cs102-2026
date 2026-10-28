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
    keyword = keyword.lower()
    key_index = 0

    for char in plaintext:
        if char.isalpha():
            shift = ord(keyword[key_index % len(keyword)]) - ord("a")

            if char.isupper():
                start = ord("A")
            else:
                start = ord("a")

            position = ord(char) - start
            new_position = (position + shift) % 26
            new_char = chr(start + new_position)
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
    keyword = keyword.lower()
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            shift = ord(keyword[key_index % len(keyword)]) - ord("a")

            if char.isupper():
                start = ord("A")
            else:
                start = ord("a")

            position = ord(char) - start
            new_position = (position - shift) % 26
            new_char = chr(start + new_position)
            plaintext += new_char

        else:
            plaintext += char

        key_index += 1

    return plaintext
