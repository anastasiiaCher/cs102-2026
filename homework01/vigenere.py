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
    keyword = keyword.upper()  # переводим ключ в заглавный регистр
    keyword_index = 0  # инициализируем счетчик для циклического перебора букв ключа
    for letter in plaintext:
        if letter.isalpha():  # проверяем, что символ является буквой
            if letter.isupper():  # обработка заглавных букв
                ciphertext += chr(
                    ((ord(letter) - ord("A")) + (ord(keyword[keyword_index % len(keyword)]) - ord("A"))) % 26 + ord(
                        "A"))
                # прибавляем к сдвигу большой буквы текста сдвиг заглавной буквы ключа, зацикливаем по %26 и возвращаем в Юникод
            elif letter.islower():  # шифруем строчные буквы
                ciphertext += chr(
                    ((ord(letter) - ord("a")) + (ord(keyword[keyword_index % len(keyword)]) - ord("A"))) % 26 + ord(
                        "a"))
                # прибавляем к сдвигу маленькой буквы текста сдвиг заглавной буквы ключа и переводим в строчный Юникод

        else:
            ciphertext += letter
        keyword_index += 1  # переход к следующему символу ключа

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
    keyword = keyword.upper()
    keyword_index_1 = 0  # инициализируем счетчик для обратного перебора букв ключа
    for letter_1 in ciphertext:
        if letter_1.isalpha():
            if letter_1.isupper():
                plaintext += chr(
                    ((ord(letter_1) - ord("A")) - (ord(keyword[keyword_index_1 % len(keyword)]) - ord("A"))) % 26 + ord(
                        "A"))
                # вычитаем сдвиг заглавной буквы ключа из сдвига большой буквы текста, зацикливаем и возвращвем в Юникод
            elif letter_1.islower():
                plaintext += chr(
                    ((ord(letter_1) - ord("a")) - (ord(keyword[keyword_index_1 % len(keyword)]) - ord("A"))) % 26 + ord(
                        "a"))
                # вычитаем сдвиг заглавной буквы ключа из сдвига маленькой буквы текста и переводим в строчный Юникод

        else:
            plaintext += letter_1
        keyword_index_1 += 1  # переходим к следующему символу ключа
    return plaintext
