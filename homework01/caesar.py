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
        if 'A' <= i <= 'Z':
            newI = (ord(i) - ord('A') + shift) % 26
            ciphertext += chr(ord('A') + newI)
        elif 'a' <= i <= 'z':
            newI = (ord(i) - ord('a') + shift) % 26
            ciphertext += chr(ord('a') + newI)
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
        if 'A' <= i <= 'Z':
            newI = (ord(i) - ord('A') - shift) % 26
            plaintext += chr(ord('A') + newI)
        elif 'a' <= i <= 'z':
            newI = (ord(i) - ord('a') - shift) % 26
            plaintext += chr(ord('a') + newI)
        else:
            plaintext += i

    return plaintext