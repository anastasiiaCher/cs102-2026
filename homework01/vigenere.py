def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    for i, k in enumerate(
        plaintext
    ):  # индекс, символ. enumerate-функция которая позволяет интегрировать plaintext в поледовательность пар
        keypass = keyword[i % len(keyword)]  # выбор буквы ключа для этого символа
        if keypass.isupper():
            shift = ord(keypass) - ord("A")
        else:
            shift = ord(keypass) - ord("a")
        if k.isupper():
            indx = ((ord(k) - ord("A")) + shift) % 26
            indx += ord("A")
            ciphertext += chr(indx)
        elif k.islower():
            indx = (ord(k) - ord("a") + shift) % 26
            indx += ord("a")
            ciphertext += chr(indx)
        else:
            ciphertext += k
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    for i, k in enumerate(ciphertext):
        keypass = keyword[i % len(keyword)]
        if keypass.isupper():
            shift = ord(keypass) - ord("A")
        else:
            shift = ord(keypass) - ord("a")
        if k.isupper():
            indx = ((ord(k) - ord("A")) - shift) % 26
            indx += ord("A")
            plaintext += chr(indx)
        elif k.islower():
            indx = (ord(k) - ord("a") - shift) % 26
            indx += ord("a")
            plaintext += chr(indx)
        else:
            plaintext += k
    return plaintext
