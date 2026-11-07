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
        if "A" <= char <= "Z":
            first_letter = "A"
        elif "a" <= char <= "z":
            first_letter = "a"
        else:
            ciphertext += char
            continue

        position = ord(char) - ord(first_letter)
        new_position = (position + shift) % 26
        ciphertext += chr(ord(first_letter) + new_position)
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
        if "A" <= char <= "Z":
            first_letter = "A"
        elif "a" <= char <= "z":
            first_letter = "a"
        else:
            plaintext += char
            continue

        position = ord(char) - ord(first_letter)
        new_position = (position - shift) % 26
        plaintext += chr(ord(first_letter) + new_position)
    return plaintext
