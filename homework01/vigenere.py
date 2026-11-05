def _vigenere(text: str, keyword: str, sign: int) -> str:
    result = ""
    for i, ch in enumerate(text):
        shift = sign * (ord(keyword[i % len(keyword)].upper()) - ord("A"))
        if "A" <= ch <= "Z":
            result += chr((ord(ch) - ord("A") + shift) % 26 + ord("A"))
        elif "a" <= ch <= "z":
            result += chr((ord(ch) - ord("a") + shift) % 26 + ord("a"))
        else:
            result += ch
    return result


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
    ciphertext = _vigenere(plaintext, keyword, 1)
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
    plaintext = _vigenere(ciphertext, keyword, -1)
    return plaintext
