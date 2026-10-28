def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a
    Caesar cipher.
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
        if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            position = ord(i) - ord("A")
            new_position = (position + shift) % 26
            ciphertext += chr(new_position + ord("A"))
        elif i in "abcdefghijklmnopqrstuvwxyz":
            position = ord(i) - ord("a")
            new_position = (position + shift) % 26
            ciphertext += chr(new_position + ord("a"))
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
        if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            position = ord(i) - ord("A")
            new_position = (position - shift) % 26
            plaintext += chr(new_position + ord("A"))
        elif i in "abcdefghijklmnopqrstuvwxyz":
            position = ord(i) - ord("a")
            new_position = (position - shift) % 26
            plaintext += chr(new_position + ord("a"))
        else:
            plaintext += i
    return plaintext
