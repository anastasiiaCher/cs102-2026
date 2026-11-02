def caesar_cipher(text: str, shift: int = 3) -> str:
    result = []

    for char in text:
        if 'A' <= char <= 'Z':
            base = ord('A')
        elif 'a' <= char <= 'z':
            base = ord('a')
        else:
            result.append(char)
            continue

        shifted = (ord(char) - base + shift) % 26
        result.append(chr(base + shifted))

    return ''.join(result)


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
    return caesar_cipher(plaintext, shift)


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
    return caesar_cipher(ciphertext, -shift)
