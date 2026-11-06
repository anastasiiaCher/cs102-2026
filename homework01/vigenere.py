def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    ciphertext = ""
    keyword = keyword.lower()
    for i in range(len(plaintext)):
        char = plaintext[i]
        if "A" <= char <= "Z":
            shift = ord(keyword[i % len(keyword)]) - ord("a")
            number = ord(char) - ord("A")
            number = (number + shift) % 26
            ciphertext += chr(number + ord("A"))
        elif "a" <= char <= "z":
            shift = ord(keyword[i % len(keyword)]) - ord("a")
            number = ord(char) - ord("a")
            number = (number + shift) % 26
            ciphertext += chr(number + ord("a"))
        else:
            ciphertext += char
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    plaintext = ""
    keyword = keyword.lower()
    for i in range(len(ciphertext)):
        char = ciphertext[i]
        if "A" <= char <= "Z":
            shift = ord(keyword[i % len(keyword)]) - ord("a")
            number = ord(char) - ord("A")
            number = (number - shift) % 26
            plaintext += chr(number + ord("A"))
        elif "a" <= char <= "z":
            shift = ord(keyword[i % len(keyword)]) - ord("a")
            number = ord(char) - ord("a")
            number = (number - shift) % 26
            plaintext += chr(number + ord("a"))
        else:
            plaintext += char
    return plaintext
