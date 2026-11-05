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

    for text_letter in plaintext:
        if text_letter.isupper():
            base = ord("A")
            text_number = ord(text_letter) - base
            key_letter = keyword[key_index % len(keyword)].upper()
            key_number = ord(key_letter) - ord("A")

            new_number = (text_number + key_number) % 26
            new_letter = chr(new_number + base)

            ciphertext += new_letter
            key_index += 1

        elif text_letter.islower():
            base = ord("a")
            text_number = ord(text_letter) - base
            key_letter = keyword[key_index % len(keyword)].lower()
            key_number = ord(key_letter) - ord("a")

            new_number = (text_number + key_number) % 26
            new_letter = chr(new_number + base)

            ciphertext += new_letter
            key_index += 1

        else:
            ciphertext += text_letter
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
    for text_letter in ciphertext:
        if text_letter.isupper():
            base = ord("A")
            text_number = ord(text_letter) - base
            key_letter = keyword[key_index % len(keyword)].upper()
            key_number = ord(key_letter) - ord("A")

            new_number = (text_number - key_number) % 26
            new_letter = chr(new_number + base)

            plaintext += new_letter
            key_index += 1

        elif text_letter.islower():
            base = ord("a")
            text_number = ord(text_letter) - base
            key_letter = keyword[key_index % len(keyword)].lower()
            key_number = ord(key_letter) - ord("a")

            new_number = (text_number - key_number) % 26
            new_letter = chr(new_number + base)

            plaintext += new_letter
            key_index += 1

        else:
            plaintext += text_letter
            key_index += 1

    return plaintext
