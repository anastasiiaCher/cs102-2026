"""
Модуль для шифрования и дешифрования текста с помощью шифра Цезаря.
"""

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
    for x in plaintext:
        if x not in "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm":
            ciphertext += x
        else:
            if x.isupper() == 1 and ord(x) + shift > 90:
                ciphertext += chr(ord(x) + shift - 26)
            elif x.isupper() == 1 and ord(x) + shift <= 90:
                ciphertext += chr(ord(x) + shift)
            if x.islower() == 1 and ord(x) + shift > 122:
                ciphertext += chr(ord(x) + shift - 26)
            elif x.islower() == 1 and ord(x) + shift <= 122:
                ciphertext += chr(ord(x) + shift)
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
    for x in ciphertext:
        if x not in "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm":
            plaintext += x
        else:
            if x.isupper() == 1 and ord(x) - shift >= 65:
                plaintext += chr(ord(x) - shift)
            elif x.isupper() == 1 and ord(x) - shift < 65:
                plaintext += chr(ord(x) - shift + 26)
            if x.islower() == 1 and ord(x) - shift >= 97:
                plaintext += chr(ord(x) - shift)
            elif x.islower() == 1 and ord(x) - shift < 97:
                plaintext += chr(ord(x) - shift + 26)
    return plaintext
