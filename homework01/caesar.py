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

    for letter in plaintext:

        if letter.islower():
            alfab_position = ord(letter) - ord("a")
            coding = (alfab_position + shift) % 26 + ord("a")
            ciphertext += chr(coding)

        elif letter.isupper():
            alfab_position = ord(letter) - ord("A")
            coding = (alfab_position + shift) % 26 + ord("A")
            ciphertext += chr(coding)

        else:
            ciphertext += letter

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
    for letter in ciphertext:

        if letter.islower():
            alfb_coding_pose = ord(letter) - ord("a")
            alfab_position = (alfb_coding_pose - shift) % 26 + ord("a")
            plaintext += chr(alfab_position)

        elif letter.isupper():
            alfb_coding_pose = ord(letter) - ord("A")
            alfab_position = (alfb_coding_pose - shift) % 26 + ord("A")
            plaintext += chr(alfab_position)

        else:
            plaintext += letter

    return plaintext
