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
    keyword = keyword.lower()
    for i in range(len(plaintext)):
        char = plaintext[i]
        if "A" <= char <= "Z":
            shift = ord(keyword[i % len(keyword)]) - ord("a")
            number = ord(char) - ord("A")
            number = (number + shift) % 26
            ciphertext += chr(number + ord("A"))
        elif "a" <= char <= "z":
            shift = ord(keyword[i % len(keyword)]) - ord("a")
            number = ord(char) - ord("a")
            number = (number + shift) % 26
            ciphertext += chr(number + ord("a"))
        else:
            ciphertext += char
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
    keyword = keyword.lower()
    for i in range(len(ciphertext)):
        char = ciphertext[i]
        if "A" <= char <= "Z":
            shift = ord(keyword[i % len(keyword)]) - ord("a")
            number = ord(char) - ord("A")
            number = (number - shift) % 26
            plaintext += chr(number + ord("A"))
        elif "a" <= char <= "z":
            shift = ord(keyword[i % len(keyword)]) - ord("a")
            number = ord(char) - ord("a")
            number = (number - shift) % 26
            plaintext += chr(number + ord("a"))
        else:
            plaintext += char
    return plaintext
