def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    ciphertext = ""
    key = keyword.lower()
    key_len = len(key)

    for i, ch in enumerate(plaintext):
        shift = ord(key[i % key_len]) - ord('a')

        if 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
            base = ord('a') if ch.islower() else ord('A')
            ciphertext += chr((ord(ch) - base + shift) % 26 + base)
        else:
            ciphertext += ch  # символ не меняем, но позицию ключа уже учли через i

    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    plaintext = ""
    key = keyword.lower()
    key_len = len(key)

    for i, ch in enumerate(ciphertext):
        shift = ord(key[i % key_len]) - ord('a')

        if 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
            base = ord('a') if ch.islower() else ord('A')
            plaintext += chr((ord(ch) - base - shift) % 26 + base)
        else:
            plaintext += ch

    return plaintext