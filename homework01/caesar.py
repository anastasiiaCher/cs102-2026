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
    for symbol in plaintext:
        if "a" <= symbol <= "z":
            start = ord("a")
        elif "A" <= symbol <= "Z":
            start = ord("A")
        else:
            ciphertext += symbol
            continue
        ciphertext += chr(start + (ord(symbol) - start + shift) % 26)
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
    for symbol in ciphertext:
        if "a" <= symbol <= "z":
            start = ord("a")
        elif "A" <= symbol <= "Z":
            start = ord("A")
        else:
            plaintext += symbol
            continue
        plaintext += chr(start + (ord(symbol) - start - shift) % 26)
    return plaintext
