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
    word2 = []
    for i in plaintext:
        if i.isalpha():
            base = ord("A") if i.isupper() else ord("a")
            word2.append(chr((ord(i) - base + shift) % 26 + base))
        else:
            word2.append(i)
    ciphertext = "".join(word2)
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
    word2 = []
    for i in ciphertext:
        if i.isalpha():
            base = ord("A") if i.isupper() else ord("a")
            word2.append(chr((ord(i) - base - shift) % 26 + base))
        else:
            word2.append(i)
    plaintext = "".join(word2)
    return plaintext
