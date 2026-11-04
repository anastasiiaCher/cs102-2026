def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    ciphertext = ""
    key_len = len(keyword)
    for i, char in enumerate(plaintext):
        shift = ord(keyword[i % key_len].lower()) - ord('a')
        if 'A' <= char <= 'Z':
            new_code = (ord(char) - ord('A') + shift) % 26 + ord('A')
            ciphertext += chr(new_code)
        elif 'a' <= char <= 'z':
            new_code = (ord(char) - ord('a') + shift) % 26 + ord('a')
            ciphertext += chr(new_code)
        else:
            ciphertext += char
    return ciphertext

def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    plaintext = ""
    key_len = len(keyword)
    for i, char in enumerate(ciphertext):
        shift = ord(keyword[i % key_len].lower()) - ord('a')
        if 'A' <= char <= 'Z':
            new_code = (ord(char) - ord('A') - shift) % 26 + ord('A')
            plaintext += chr(new_code)
        elif 'a' <= char <= 'z':
            new_code = (ord(char) - ord('a') - shift) % 26 + ord('a')
            plaintext += chr(new_code)
        else:
            plaintext += char
    return plaintext
