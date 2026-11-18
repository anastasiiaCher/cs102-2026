
# ord("A") → 65: «какой номер у этого символа?»
# chr(65) → "A": «какой символ стоит под этим номером?»


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
    for i, char in enumerate(plaintext):
        keychar = keyword[i % len(keyword)] # закольцевали - выдает букву ключ-сл
        shift = ord(keychar.upper()) - 65 # вычисляем сдвиг
        if "A" <= char <= "Z":
            ciphertext += chr((ord(char) - 65 + shift) % 26 + 65)
        elif "a" <= char <= "z":
            ciphertext += chr((ord(char) + shift - 97) % 26 + 97)
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
    for i, char in enumerate(ciphertext):
        keychar = keyword[i % len(keyword)] # закольцевали - выдает букву ключ-сл
        shift = ord(keychar.upper()) - 65 # вычисляем сдвиг
        if "A" <= char <= "Z":
            plaintext += chr((ord(char) - 65 - shift) % 26 + 65)
        elif "a" <= char <= "z":
            plaintext += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            plaintext += char
    return plaintext