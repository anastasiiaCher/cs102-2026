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
    # PUT OUR CODE HERE
    ciphertext = ""
    key_index = 0
    
    for char in plaintext:
        if char.isalpha():
            shift = ord(keyword[key_index % len(keyword)].upper()) - 65
            is_upper = char.isupper()
            char_code = ord(char.upper()) - 65
            new_code = (char_code + shift) % 26
            new_char = chr(new_code + 65)
            if not is_upper:
                new_char = new_char.lower()
            ciphertext += new_char
            key_index += 1
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
    plaintext = ""
    key_index = 0
    for char in ciphertext:
        if char.isalpha():
            shift = ord(keyword[key_index % len(keyword)].upper()) - 65
            is_upper = char.isupper()
            char_code = ord(char.upper()) - 65
            new_code = (char_code - shift) % 26
            new_char = chr(new_code + 65)
            if not is_upper:
                new_char = new_char.lower()
            plaintext += new_char
            key_index += 1
        else:
            plaintext += char
    return plaintext
