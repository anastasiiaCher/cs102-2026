from caesar import encrypt_caesar


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
    if not keyword or any(not ("a" <= char <= "z") for char in keyword.lower()):
        raise ValueError("Keyword must contain only ASCII letters and cannot be empty.")
    keyword = keyword.lower()
    for index, char in enumerate(plaintext):
        shift = ord(keyword[index % len(keyword)]) - ord("a")
        ciphertext += encrypt_caesar(char, shift)
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
    if not keyword or any(not ("a" <= char <= "z") for char in keyword.lower()):
        raise ValueError("Keyword must contain only ASCII letters and cannot be empty.")
    keyword = keyword.lower()
    for index, char in enumerate(ciphertext):
        shift = ord(keyword[index % len(keyword)]) - ord("a")
        plaintext += encrypt_caesar(char, -shift)
    return plaintext
