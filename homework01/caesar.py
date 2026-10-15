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
    upper_ind = ord("A")
    lower_ind = ord("a")
    alpha_size = 26
    for c in plaintext:
        if c.isupper():
            ciphertext += chr((ord(c) - upper_ind + shift) % alpha_size + upper_ind)
        elif c.islower():
            ciphertext += chr((ord(c) - lower_ind + shift) % alpha_size + lower_ind)
        else:
            ciphertext += c
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
    upper_ind = ord("A")
    lower_ind = ord("a")
    alpha_size = 26
    for character in ciphertext:
        if character.isupper():
            plaintext += chr((ord(character) - upper_ind - shift) % alpha_size + upper_ind)
        elif character.islower():
            plaintext += chr((ord(character) - lower_ind - shift) % alpha_size + lower_ind)
        else:
            plaintext += character
    return plaintext
