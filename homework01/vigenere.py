def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    """
    ciphertext = ""
    key_index = 0
    for ch in plaintext:
        if ch.isalpha():
            shift = ord(keyword[key_index % len(keyword)].upper()) - ord("A")
            if ch.isupper():
                ciphertext += chr((ord(ch) - ord("A") + shift) % 26 + ord("A"))
            else:
                ciphertext += chr((ord(ch) - ord("a") + shift) % 26 + ord("a"))
            key_index += 1
        else:
            ciphertext += ch
    return ciphertext

def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    """
    plaintext = ""
    key_index = 0
    for ch in ciphertext:
        if ch.isalpha():
            shift = ord(keyword[key_index % len(keyword)].upper()) - ord("A")
            if ch.isupper():
                plaintext += chr((ord(ch) - ord("A") - shift) % 26 + ord("A"))
            else:
                plaintext += chr((ord(ch) - ord("a") - shift) % 26 + ord("a"))
            key_index += 1
        else:
            plaintext += ch
    return plaintext
