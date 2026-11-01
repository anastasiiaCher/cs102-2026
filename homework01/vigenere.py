def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    ciphertext = ""
    key_index = 0

    for char in plaintext:
        if char.isalpha():
            key_char = keyword[key_index % len(keyword)].lower()
            shift = ord(key_char) - ord("a")
            base = ord("A") if char.isupper() else ord("a")
            encrypted_char = chr((ord(char) - base + shift) % 26 + base)
            ciphertext += encrypted_char
        else:
            ciphertext += char

        key_index += 1

    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    plaintext = ""
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            key_char = keyword[key_index % len(keyword)].lower()
            shift = ord(key_char) - ord("a")
            base = ord("A") if char.isupper() else ord("a")
            decrypted_char = chr((ord(char) - base - shift) % 26 + base)
            plaintext += decrypted_char
        else:
            plaintext += char

        key_index += 1

    return plaintext
