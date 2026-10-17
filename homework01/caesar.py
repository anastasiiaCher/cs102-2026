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
    shift = shift % 26
    for letter in plaintext:
        if letter.isalpha():  # проверка, является ли символ буквой
            if letter.isupper():  # обработка заглавной буквы
                big_letter = chr((ord(letter) - ord("A") + shift) % 26 + ord(
                    "A"))  # приводим к индексу 0-25, сдвигаем, зацикливаем через %26, переводим обратно в символ Юникода
                ciphertext += big_letter
            elif letter.islower():  # обработка строчной буквы
                lil_letter = chr((ord(letter) - ord("a") + shift) % 26 + ord("a"))
                ciphertext += lil_letter
        else:  # если это пробел или знак препинания, оставляем как есть
            ciphertext += letter
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
    shift = shift % 26
    for letter_1 in ciphertext:
        if letter_1.isalpha():  # проверка, является ли символ буквой
            if letter_1.isupper():  # обработка заглавных букв
                new_letter_1 = chr((ord(letter_1) - ord("A") - shift) % 26 + ord(
                    "A"))  # переводим в индекс 0-25, сдвигаем назад, зацикливаем и возвращаем в Юникод
                plaintext += new_letter_1
            elif letter_1.islower():  # обработка строчных букв
                new_letter_2 = chr((ord(letter_1) - ord("a") - shift) % 26 + ord("a"))
                plaintext += new_letter_2
        else:  # если это пробел или знак препинания, оставляем, как есть
            plaintext += letter_1

    return plaintext
