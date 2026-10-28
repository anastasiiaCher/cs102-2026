def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    ciphertext = ""
    word1 = list(plaintext)
    key = list(keyword)
    word2 = []
    for i in range(len(plaintext)):
        if word1[i].isalpha():
            base = ord("A") if word1[i].isupper() else ord("a")
            if key[i % len(keyword)].isalpha():
                base1 = ord("A") if key[i % len(keyword)].isupper() else ord("a")
                word2.append(chr((ord(word1[i]) - base + ord(key[i % len(keyword)]) - base1) % 26 + base))
            else:
                word2.append(word1[i])
        else:
            word2.append(word1[i])
    ciphertext = "".join(word2)
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    word1 = list(ciphertext)
    key = list(keyword)
    word2 = []
    for i in range(len(ciphertext)):
        if word1[i].isalpha():
            base = ord("A") if word1[i].isupper() else ord("a")
            if key[i % len(keyword)].isalpha():
                base1 = ord("A") if key[i % len(keyword)].isupper() else ord("a")
                word2.append(chr((ord(word1[i]) - base - ord(key[i % len(keyword)]) + base1) % 26 + base))
            else:
                word2.append(word1[i])
        else:
            word2.append(word1[i])
    plaintext = "".join(word2)
    return plaintext
