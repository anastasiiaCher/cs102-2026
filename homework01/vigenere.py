def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    ciphertext = ""
    key_index = 0

    for char in plaintext:
        shift = ord(keyword[key_index % len(keyword)].upper()) - ord("A")

        if "A" <= char <= "Z":
            ciphertext += chr(
                (ord(char) - ord("A") + shift) % 26 + ord("A")
            )

        elif "a" <= char <= "z":
            ciphertext += chr(
                (ord(char) - ord("a") + shift) % 26 + ord("a")
            )

        else:
            ciphertext += char

        key_index += 1

    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    plaintext = ""
    key_index = 0

    for char in ciphertext:
        shift = ord(keyword[key_index % len(keyword)].upper()) - ord("A")

        if "A" <= char <= "Z":
            plaintext += chr(
                (ord(char) - ord("A") - shift) % 26 + ord("A")
            )

        elif "a" <= char <= "z":
            plaintext += chr(
                (ord(char) - ord("a") - shift) % 26 + ord("a")
            )

        else:
            plaintext += char

        key_index += 1

    return plaintext