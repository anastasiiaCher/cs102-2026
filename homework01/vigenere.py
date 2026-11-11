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

    for letter in plaintext:
        if letter.islower():

            key_char = keyword[key_index % len(keyword)]
            shift = ord(key_char.lower()) - ord("a")

            alfab_position = ord(letter) - ord("a")
            coding = (alfab_position + shift) % 26 + ord("a")
            ciphertext += chr(coding)

        elif letter.isupper():

            key_char = keyword[key_index % len(keyword)]
            shift = ord(key_char.upper()) - ord("A")

            alfab_position = ord(letter) - ord("A")
            coding = (alfab_position + shift) % 26 + ord("A")
            ciphertext += chr(coding)

        else:
            ciphertext += letter

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

    for letter in ciphertext:
        if letter.islower():

            key_char = keyword[key_index % len(keyword)]
            shift = ord(key_char.lower()) - ord("a")

            current_position = ord(letter) - ord("a")
            uncoding = (current_position - shift) % 26 + ord("a")
            plaintext += chr(uncoding)

        elif letter.isupper():

            key_char = keyword[key_index % len(keyword)]
            shift = ord(key_char.upper()) - ord("A")

            current_position = ord(letter) - ord("A")
            uncoding = (current_position - shift) % 26 + ord("A")
            plaintext += chr(uncoding)

        else:
            plaintext += letter
        key_index += 1

    return plaintext
