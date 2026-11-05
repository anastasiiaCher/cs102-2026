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
    for ch in plaintext:
        if ch.isupper():
            ciphertext += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
        elif ch.islower():
            ciphertext += chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
        else:
            ciphertext += ch
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
    for ch in ciphertext:
        if ch.isupper():
            plaintext += chr((ord(ch) - ord('A') - shift) % 26 + ord('A'))
        elif ch.islower():
            plaintext += chr((ord(ch) - ord('a') - shift) % 26 + ord('a'))
        else:
            plaintext += ch
    return plaintext