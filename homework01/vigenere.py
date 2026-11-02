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
    for element in plaintext:
        if element.isalpha():
            shift = ord(keyword[keyin % len(keyword)]) - ord("A")
            base = ord("A") if element.isupper() else ord("a")
            new = (ord(element) - base + shift) % 26 + base
            ciphertext += chr(new)
        else:
            ciphertext += element
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
    for element in ciphertext:
        if element.isalpha():
            shift = ord(keyword[keyin % len(keyword)]) - ord("A")
            base = ord("A") if element.isupper() else ord("a")
            new = (ord(element) - base - shift) % 26 + base
            plaintext += chr(new)
        else:
            plaintext += element
        keyin += 1
    return plaintext
