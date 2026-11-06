def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    ciphertext = ""
    for char in plaintext:
        if "A" <= char <= "Z":
            number = ord(char) - ord("A")
            number = (number + shift) % 26
            ciphertext += chr(number + ord("A"))
        elif "a" <= char <= "z":
            number = ord(char) - ord("a")
            number = (number + shift) % 26
            ciphertext += chr(number + ord("a"))
        else:
            ciphertext += char
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    plaintext = ""
    for char in ciphertext:
        if "A" <= char <= "Z":
            number = ord(char) - ord("A")
            number = (number - shift) % 26
            plaintext += chr(number + ord("A"))
        elif "a" <= char <= "z":
            number = ord(char) - ord("a")
            number = (number - shift) % 26
            plaintext += chr(number + ord("a"))
        else:
            plaintext += char
    return plaintext
