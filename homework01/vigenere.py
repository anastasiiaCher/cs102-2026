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
        # Сдвигаем индекс ключа для КАЖДОГО символа
        key_char = keyword[key_index % len(keyword)]
        shift = ord(key_char.upper()) - ord("A")

        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            shifted_code = (ord(char) - base + shift) % 26
            ciphertext += chr(base + shifted_code)
        else:
            # Не буквы добавляем как есть, но ключ уже сдвинулся выше
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
        # Сдвигаем индекс ключа для КАЖДОГО символа
        key_char = keyword[key_index % len(keyword)]
        shift = ord(key_char.upper()) - ord("A")

        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            shifted_code = (ord(char) - base - shift) % 26
            plaintext += chr(base + shifted_code)
        else:
            plaintext += char

        key_index += 1

    return plaintext
