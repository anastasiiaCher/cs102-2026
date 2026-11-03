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
        if letter.isupper():
            base = ord("A")
            number = ord(letter)
            new_number = (number - base + shift) % 26 + base
            new_letter = chr(new_number)
            ciphertext += new_letter

        elif letter.islower():
            base = ord("a")
            number = ord(letter)
            new_number = (number - base + shift) % 26 + base
            new_letter = chr(new_number)
            ciphertext += new_letter
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
    # PUT YOUR CODE HERE
    return plaintext