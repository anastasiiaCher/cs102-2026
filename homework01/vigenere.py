def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    """
    ciphertext = ""
    key_index = 0
    for ch in plaintext:
        if 'A' <= ch <= 'Z':
            shift = ord(keyword[key_index % len(keyword)].upper()) - ord('A')
            ciphertext += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
            key_index += 1
        elif 'a' <= ch <= 'z':
            shift = ord(keyword[key_index % len(keyword)].upper()) - ord('A')
            ciphertext += chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
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
        if 'A' <= ch <= 'Z':
            shift = ord(keyword[key_index % len(keyword)].upper()) - ord('A')
            plaintext += chr((ord(ch) - ord('A') - shift) % 26 + ord('A'))
            key_index += 1
        elif 'a' <= ch <= 'z':
            shift = ord(keyword[key_index % len(keyword)].upper()) - ord('A')
            plaintext += chr((ord(ch) - ord('a') - shift) % 26 + ord('a'))
            key_index += 1
        else:
            plaintext += ch
    return plaintext