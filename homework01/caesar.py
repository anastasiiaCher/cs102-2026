def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for element in plaintext:
        if element.isalpha():
            base = ord("A") if element.isupper() else ord("a")
            new = (ord(element) - base + shift) % 26 + base
            ciphertext += chr(new)
        else:
            ciphertext += element

    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    for element in ciphertext:
        if element.isalpha():
            base = ord("A") if element.isupper() else ord("a")
            new = (ord(element) - base - shift) % 26 + base
            plaintext += chr(new)
        else:
            plaintext += element
    return plaintext
