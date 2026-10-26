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
        if i.isalpha():
            if i == i.lower():
                place = ord(i) - ord("a")
                new_place = (place + shift) % 26
                k = chr(new_place + ord("a"))
                ciphertext += k
            else:
                place = ord(i) - ord("A")
                new_place = (place + shift) % 26
                k = chr(new_place + ord("A"))
                ciphertext += k
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
        if i.isalpha():
            if i == i.lower():
                place = ord(i) - ord("a")
                new_place = (place - shift) % 26
                k = chr(new_place + ord("a"))
                plaintext += k
            else:
                place = ord(i) - ord("A")
                new_place = (place - shift) % 26
                k = chr(new_place + ord("A"))
                plaintext += k
        else:
            plaintext += i

    return plaintext
