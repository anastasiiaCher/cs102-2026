def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
    """
    ciphertext = ""
    for char in plaintext:
        if char.isupper():
            # Шифрование заглавных английских букв (A-Z)
            ciphertext += chr((ord(char) - ord("A") + shift) % 26 + ord("A"))
        elif char.islower():
            # Шифрование строчных английских букв (a-z)
            ciphertext += chr((ord(char) - ord("a") + shift) % 26 + ord("a"))
        else:
            # Все остальные символы (цифры, знаки препинания) остаются как есть
            ciphertext += char

    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.
    """
    plaintext = ""
    for char in ciphertext:
        if char.isupper():
            # Дешифрование заглавных английских букв
            plaintext += chr((ord(char) - ord("A") - shift) % 26 + ord("A"))
        elif char.islower():
            # Дешифрование строчных английских букв
            plaintext += chr((ord(char) - ord("a") - shift) % 26 + ord("a"))
        else:
            # Символы без изменений
            plaintext += char

    return plaintext
