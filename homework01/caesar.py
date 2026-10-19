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
        if symbol.isalpha():
            shift_start = ord("A") if symbol.isupper() else ord("a")
            encrypted_symbol = chr((ord(symbol) - shift_start + shift) % 26 + shift_start)
            ciphertext += encrypted_symbol
        else:
            ciphertext += symbol
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
        if symbol.isalpha():
            shift_start = ord("A") if symbol.isupper() else ord("a")
            decrypted_symbol = chr((ord(symbol) - shift_start - shift) % 26 + shift_start)
            plaintext += decrypted_symbol
        else:
            plaintext += symbol
    return plaintext
