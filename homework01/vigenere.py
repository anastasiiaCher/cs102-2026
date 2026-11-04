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
    # PUT YOUR CODE HERE
    for i, char in enumerate(plaintext):
        key_char = keyword[i % len(keyword)]
        shift = ord(key_char.lower()) - ord("a")
        if "a" <= char <= "z":
            ciphertext += chr((ord(char) - ord("a") + shift) % 26 + ord("a"))
        elif "A" <= char <= "Z":
            ciphertext += chr((ord(char) - ord("A") + shift) % 26 + ord("A"))
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
    # PUT YOUR CODE HERE
    for i, char in enumerate(ciphertext):
        key_char = keyword[i % len(keyword)]
        shift = ord(key_char.lower()) - ord("a")
        if "a" <= char <= "z":
            plaintext += chr((ord(char) - ord("a") - shift) % 26 + ord("a"))
        elif "A" <= char <= "Z":
            plaintext += chr((ord(char) - ord("A") - shift) % 26 + ord("A"))
        else:
            plaintext += char
    return plaintext
