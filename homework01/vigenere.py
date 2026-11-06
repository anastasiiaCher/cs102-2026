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
    for i in range(len(plaintext)):
        char = plaintext[i]
        shift = ord(keyword[i % len(keyword)].upper()) - ord("A")
        if char.isalpha():
            if 65 <= ord(char) <= 90:
                ciphertext += chr((ord(char) - ord("A") + shift) % 26 + ord("A"))
            elif 97 <= ord(char) <= 122:
                ciphertext += chr((ord(char) - ord("a") + shift) % 26 + ord("a"))
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
    for i in range(len(ciphertext)):
        char = ciphertext[i]
        shift = ord(keyword[i % len(keyword)].upper()) - ord("A")
        if char.isalpha():
            if 65 <= ord(char) <= 90:
                plaintext += chr((ord(char) - ord("A") - shift) % 26 + ord("A"))
            elif 97 <= ord(char) <= 122:
                plaintext += chr((ord(char) - ord("a") - shift) % 26 + ord("a"))
        else:
            plaintext += char
    return plaintext
