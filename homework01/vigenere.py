def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    """
    ciphertext = ""
    keyword_length = len(keyword)
    key_index = 0

    for char in plaintext:
        if char.isalpha():
            key_char = keyword[key_index % keyword_length]
            shift = ord(key_char.upper()) - ord("A")

            if char.isupper():
                ciphertext += chr((ord(char) - ord("A") + shift) % 26 + ord("A"))
            elif char.islower():
                ciphertext += chr((ord(char) - ord("a") + shift) % 26 + ord("a"))
        else:
            ciphertext += char

        # Переносим инкремент сюда, чтобы он увеличивался ДЛЯ ВСЕХ символов
        key_index += 1

    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    """
    plaintext = ""
    keyword_length = len(keyword)
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            key_char = keyword[key_index % keyword_length]
            shift = ord(key_char.upper()) - ord("A")

            if char.isupper():
                plaintext += chr((ord(char) - ord("A") - shift) % 26 + ord("A"))
            elif char.islower():
                plaintext += chr((ord(char) - ord("a") - shift) % 26 + ord("a"))
        else:
            plaintext += char

        # Переносим инкремент сюда, чтобы он увеличивался ДЛЯ ВСЕХ символов
        key_index += 1

    return plaintext
