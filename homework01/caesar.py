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
        if 'A' <= char <= 'Z':
            # Сдвиг для заглавных букв (код 'A' = 65)
            new_code = (ord(char) - ord('A') + shift) % 26 + ord('A')
            ciphertext += chr(new_code)
        elif 'a' <= char <= 'z':
            # Сдвиг для строчных букв (код 'a' = 97)
            new_code = (ord(char) - ord('a') + shift) % 26 + ord('a')
            ciphertext += chr(new_code)
        else:
            # Если это не буква (цифры, точки и т.д.), оставляем без изменений
            ciphertext += char  # PUT YOUR CODE HERE
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
        if 'A' <= char <= 'Z':
            new_code = (ord(char) - ord('A') - shift) % 26 + ord('A')
            plaintext += chr(new_code)
        elif 'a' <= char <= 'z':
            new_code = (ord(char) - ord('a') - shift) % 26 + ord('a')
            plaintext += chr(new_code)
        else:
            plaintext += char
    return plaintext
