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
    cyphertext = ""
    upper_ind = ord("A")
    lower_ind = ord("a")
    alpha_size = 26
    while len(keyword) < len(plaintext):
        keyword += keyword
    for i, j in zip(plaintext, keyword):
        if j.isupper():
            shift = ord(j) - upper_ind
        else:
            shift = ord(j) - lower_ind
        if i.isupper():
            cyphertext += chr((ord(i) - upper_ind + shift) % alpha_size + upper_ind)
        elif i.islower():
            cyphertext += chr((ord(i) - lower_ind + shift) % alpha_size + upper_ind)
        else:
            cyphertext += i
    return cyphertext


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
    upper_ind = ord("A")
    lower_ind = ord("a")
    alpha_size = 26
    while len(keyword) < len(ciphertext):
        keyword += keyword
    for i, j in zip(ciphertext, keyword):
        if j.isupper():
            shift = ord(j) - upper_ind
        else:
            shift = ord(j) - lower_ind
        if i.isupper():
            plaintext += chr((ord(i) - upper_ind - shift) % alpha_size + upper_ind)
        elif i.islower():
            plaintext += chr((ord(i) - lower_ind - shift) % alpha_size + upper_ind)
        else:
            plaintext += i
    return plaintext
