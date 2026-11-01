def validate_keyword(keyword: str) -> None:
    if not keyword or not keyword.isascii() or not keyword.isalpha():
        raise ValueError("Keyword must contain only Latin letters")



def vigenere(text: str, keyword: str, decrypt: bool = False) -> str:
    if not keyword or not keyword.isascii() or not keyword.isalpha():
        raise ValueError("Keyword must contain only Latin letters")

    keyword = keyword.upper()
    result = []

    for i, char in enumerate(text):
        if not char.isascii() or not char.isalpha():
            result.append(char)
            continue

        shift = ord(keyword[i % len(keyword)]) - ord('A')

        if decrypt:
            shift = -shift

        base = ord('A') if char.isupper() else ord('a')
        shifted = (ord(char) - base + shift) % 26

        result.append(chr(base + shifted))

    return ''.join(result)


def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    return vigenere(plaintext, keyword)


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    return vigenere(ciphertext, keyword, decrypt=True)


