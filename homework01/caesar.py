"""
Модуль для шифрования и дешифрования текста с помощью шифра Цезаря.
"""

UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWER = "abcdefghijklmnopqrstuvwxyz"
KOLVO_BUKV_V_ALFAVITE = 26


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for x in plaintext:
        if x in LOWER:
            ciphertext += LOWER[(LOWER.index(x) + shift) % KOLVO_BUKV_V_ALFAVITE]
            # берём индекс сначала от номера маленькоц
            # буквы в алфивите и добавляем сдивг, дальше делаем на число букв в алфаите (26)
            # , чтобы мы вернились в границы алфавита и опять определяем,
            # какая это буква в алфавите по счёту
        elif x in UPPER:
            ciphertext += UPPER[(UPPER.index(x) + shift) % KOLVO_BUKV_V_ALFAVITE]  # аналогично
        else:
            ciphertext += x  # скипаем не буквы (не прининяем сдвиг, просто дописываем к результат)
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    # PUT YOUR CODE HERE
    for x in ciphertext:
        # аналогично
        if x in UPPER:
            plaintext += UPPER[(UPPER.index(x) - shift) % KOLVO_BUKV_V_ALFAVITE]
        elif x in LOWER:
            plaintext += LOWER[(LOWER.index(x) - shift) % KOLVO_BUKV_V_ALFAVITE]
        else:
            plaintext += x
    return plaintext
