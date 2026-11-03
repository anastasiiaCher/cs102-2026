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
    key_len = len(keyword)
    key_index = 0

    for ch in plaintext:
        if "A" <= ch <= "Z":
            shift = ord(keyword[key_index % key_len]) - ord("A")
            ciphertext += chr((ord(ch) - ord("A") + shift) % 26 + ord("A"))
        elif "a" <= ch <= "z":
            shift = ord(keyword[key_index % key_len].lower()) - ord("a")
            ciphertext += chr((ord(ch) - ord("a") + shift) % 26 + ord("a"))
        else:
            ciphertext += ch
        key_index += 1  # ← ВАЖНО: увеличиваем для ВСЕХ символов
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
    key_len = len(keyword)
    key_index = 0

    for ch in ciphertext:
        if "A" <= ch <= "Z":
            shift = ord(keyword[key_index % key_len]) - ord("A")
            plaintext += chr((ord(ch) - ord("A") - shift) % 26 + ord("A"))
        elif "a" <= ch <= "z":
            shift = ord(keyword[key_index % key_len].lower()) - ord("a")
            plaintext += chr((ord(ch) - ord("a") - shift) % 26 + ord("a"))
        else:
            plaintext += ch
        key_index += 1  # ← ВАЖНО: увеличиваем для ВСЕХ символов
    return plaintext
