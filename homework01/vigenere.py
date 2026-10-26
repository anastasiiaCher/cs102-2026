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

    for ind, i in enumerate(plaintext):
        if i.isalpha():
            if i == i.lower():
                place = ord(i) - ord("a")
                current_key = keyword[ind % len(keyword)]
                shift = ord(current_key) - ord("a")
                new_place = (place + shift) % 26
                k = chr(new_place + ord("a"))
                ciphertext += k
            else:
                place = ord(i) - ord("A")
                current_key = keyword[ind % len(keyword)].upper()
                shift = ord(current_key) - ord("A")
                new_place = (place + shift) % 26
                k = chr(new_place + ord("A"))
                ciphertext += k
        else:
            ciphertext += i

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

    for ind, i in enumerate(ciphertext):
        if i.isalpha():
            if i == i.lower():
                place = ord(i) - ord("a")
                current_key = keyword[ind % len(keyword)]
                shift = ord(current_key) - ord("a")
                new_place = (place - shift) % 26
                k = chr(new_place + ord("a"))
                plaintext += k
            else:
                place = ord(i) - ord("A")
                current_key = keyword[ind % len(keyword)].upper()
                shift = ord(current_key) - ord("A")
                new_place = (place - shift) % 26
                k = chr(new_place + ord("A"))
                plaintext += k
        else:
            plaintext += i

    return plaintext
