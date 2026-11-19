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
    keyword = keyword.upper()
    key_index = 0

    for char in plaintext:
        if char.isalpha():
            letter_in_key = keyword[key_index % len(keyword)]
            shift = ord(letter_in_key) - ord("A")

            if char.isupper():
                code = ord(char) - ord("A")
                code = (code + shift) % 26
                code = code + ord("A")
                ciphertext = ciphertext + chr(code)
            else:
                code = ord(char) - ord("a")
                code = (code + shift) % 26
                code = code + ord("a")
                ciphertext = ciphertext + chr(code)

        else:
            ciphertext = ciphertext + char
        key_index = key_index + 1
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
    keyword = keyword.upper()
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            letter_in_key = keyword[key_index % len(keyword)]
            shift = ord(letter_in_key) - ord("A")

            if char.isupper():
                code = ord(char) - ord("A")
                code = (code - shift + 26) % 26
                code = code + ord("A")
                plaintext = plaintext + chr(code)
            else:
                code = ord(char) - ord("a")
                code = (code - shift + 26) % 26
                code = code + ord("a")
                plaintext = plaintext + chr(code)

        else:
            plaintext = plaintext + char
        key_index = key_index + 1

    return plaintext
