def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    if not keyword:
        return plaintext
    ciphertext = ""
    key_index = 0
    for ch in plaintext:
        shift = ord(keyword[key_index % len(keyword)].upper()) - ord('A')
        if 'A' <= ch <= 'Z':
            ciphertext += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
        elif 'a' <= ch <= 'z':
            ciphertext += chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
        else:
            ciphertext += ch
        key_index += 1
    return ciphertext

def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    if not keyword:
        return ciphertext
    plaintext = ""
    key_index = 0
    for ch in ciphertext:
        shift = ord(keyword[key_index % len(keyword)].upper()) - ord('A')
        if 'A' <= ch <= 'Z':
            plaintext += chr((ord(ch) - ord('A') - shift) % 26 + ord('A'))
        elif 'a' <= ch <= 'z':
            plaintext += chr((ord(ch) - ord('a') - shift) % 26 + ord('a'))
        else:
            plaintext += ch
        key_index += 1
    return plaintext