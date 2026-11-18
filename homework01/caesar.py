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
    for char in plaintext:
        if char.isupper():
            code = ord(char) - ord('A')
            code = code + shift
            code = code % 26
            code = code + ord('A')
            ciphertext = ciphertext + chr(code)
        elif char.islower():
            code = ord(char) - ord('a')
            code = code + shift
            code = code % 26
            code = code + ord('a')
            ciphertext = ciphertext + chr(code)
        else:
            ciphertext = ciphertext + char    

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
    for char in ciphertext:
        if char.isupper():
            code = ord(char) - ord('A')
            code = code - shift
            code = code % 26
            code = code + ord('A')
            plaintext = plaintext + chr(code)
        elif char.islower():
            code = ord(char) - ord('a')
            code = code - shift
            code = code % 26
            code = code + ord('a')
            plaintext = plaintext + chr(code)
        else:
            plaintext = plaintext + char
    return plaintext