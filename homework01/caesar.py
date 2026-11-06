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
    # PUT YOUR CODE HERE
    for i in plaintext:
        if i.isalpha():
            if 65<=ord(i)<=90:
                ciphertext+= chr((ord(i) - ord("A") + shift) % 26 + ord("A"))
            elif 97<=ord(i)<=122:
                ciphertext += chr((ord(i) - ord('a') + shift) % 26 + ord('a'))
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
    # PUT YOUR CODE HERE
    for i in ciphertext:
        if i.isalpha():
            if 65<=ord(i)<=90:
                plaintext+= chr((ord(i) - ord("A") - shift) % 26 + ord("A"))
            elif 97<=ord(i)<=122:
                plaintext += chr((ord(i) - ord('a') - shift) % 26 + ord('a'))
        else:
            plaintext += i
    return plaintext