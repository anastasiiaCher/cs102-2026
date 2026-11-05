def _shift_text(text: str, shift: int) -> str:
    result = ""
    for ch in text:
        if "A" <= ch <= "Z":
            result += chr((ord(ch) - ord("A") + shift) % 26 + ord("A"))
        elif "a" <= ch <= "z":
            result += chr((ord(ch) - ord("a") + shift) % 26 + ord("a"))
        else:
            result += ch
    return result


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
    ciphertext = _shift_text(plaintext, shift)
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
    plaintext = _shift_text(ciphertext, -shift)
    return plaintext
