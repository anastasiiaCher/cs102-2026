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
    keyword_index = 0
    for char in plaintext:
        if char.isalpha():
            shift = ord(keyword[keyword_index % len(keyword)]) - ord('A')
            base = ord('A') if char.isupper() else ord('a')
            ciphertext += chr((ord(char) - base + shift) % 26 + base)
        else:
            ciphertext += char
        keyword_index += 1
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
    keyword_index = 0
    for char in ciphertext:
        if char.isalpha():
            shift = ord(keyword[keyword_index % len(keyword)]) - ord('A')
            base = ord('A') if char.isupper() else ord('a')
            plaintext += chr((ord(char) - base - shift) % 26 + base)
        else:
            plaintext += char
        keyword_index += 1
    return plaintext
