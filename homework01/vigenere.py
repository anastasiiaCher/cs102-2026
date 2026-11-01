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
    keyin = 0
    for i in plaintext:
        if i.isalpha():
            shift = ord(keyword[keyin % len(keyword)]) - ord("A")
            b = ord("A") if i.isupper() else ord("a")
            new = (ord(i) - b + shift) % 26 + b
            ciphertext += chr(new)
        else:
            ciphertext += i
        keyin += 1
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
    keyin = 0
    for i in ciphertext:
        if i.isalpha():
            shift = ord(keyword[keyin % len(keyword)]) - ord("A")
            b = ord("A") if i.isupper() else ord("a")
            new = (ord(i) - b - shift) % 26 + b
            plaintext += chr(new)
        else:
            plaintext += i
        keyin += 1
    return plaintext