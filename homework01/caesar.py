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
    for i in plaintext:
        if "a" <= i <= "z":
            ciphertext += chr((ord(i) - ord("a") + shift) % 26 + ord("a"))
        elif "A" <= i <= "Z":
            ciphertext += chr((ord(i) - ord("A") + shift) % 26 + ord("A"))
        else:
            ciphertext += i
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
    for i in ciphertext:
        if "a" <= i <= "z":
            plaintext += chr((ord(i) - ord("a") - shift) % 26 + ord("a"))
        elif "A" <= i <= "Z":
            plaintext += chr((ord(i) - ord("A") - shift) % 26 + ord("A"))
        else:
            plaintext += i

    return plaintext
