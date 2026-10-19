"""
Модуль для шифрования и дешифрования текста с помощью шифра Цезаря
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
    for char in plaintext:
        if not ("A" <= char <= "Z" or "a" <= char <= "z"):
            ciphertext += char
        else:
            if char.isupper() and ord(char) + shift > ord("Z") or char.islower() and ord(char) + shift > ord("z"):
                ciphertext += chr(ord(char) + shift - 26)
            elif char.isupper() and ord(char) + shift <= ord("Z") or char.islower() and ord(char) + shift <= ord("z"):
                ciphertext += chr(ord(char) + shift)
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
    for char in ciphertext:
        if not ("A" <= char <= "Z" or "a" <= char <= "z"):
            plaintext += char
        else:
            if char.isupper() and ord(char) - shift < ord("A") or char.islower() == 1 and ord(char) - shift < ord("a"):
                plaintext += chr(ord(char) - shift + 26)
            elif char.isupper() and ord(char) - shift >= ord("A") or char.islower() and ord(char) - shift >= ord("a"):
                plaintext += chr(ord(char) - shift)
    return plaintext
