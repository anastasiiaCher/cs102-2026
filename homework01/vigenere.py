def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    j = 0  # keyword index
    for i in plaintext:
        if "a" <= i <= "z":
            ciphertext += chr(
                (ord(i) - ord("a") + ord(keyword[j % len(keyword)].lower()) - ord("a"))
                % 26
                + ord("a")
            )
            j += 1
        elif "A" <= i <= "Z":
            ciphertext += chr(
                (ord(i) - ord("A") + ord(keyword[j % len(keyword)]) - ord("A")) % 26
                + ord("A")
            )
            j += 1
        else:
            ciphertext += i
            j += 1
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
    j = 0  # keyword index
    for i in ciphertext:
        if "a" <= i <= "z":
            plaintext += chr(
                (
                    ord(i)
                    - ord("a")
                    - (ord(keyword[j % len(keyword)].lower()) - ord("a"))
                )
                % 26
                + ord("a")
            )
            j += 1
        elif "A" <= i <= "Z":
            plaintext += chr(
                (ord(i) - ord("A") - (ord(keyword[j % len(keyword)]) - ord("A"))) % 26
                + ord("A")
            )
            j += 1
        else:
            plaintext += i
            j += 1
    return plaintext
