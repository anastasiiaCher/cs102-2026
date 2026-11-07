"""
Encrypts plaintext using a Vigenere cipher.
>>> encrypt_vigenere("PYTHON", "A")
'PYTHON'
>>> encrypt_vigenere("python", "a")
'python'
>>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
'LXFOPVEFRNHR'
"""


def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    ciphertext = ""  # создаем пустую строку чтоюы записать туда зашифрованный текст
    keyword_index = 0  # индекс буквы которую мы рассматриваем в ключе
    for char in plaintext:  # рассматриваем символы в простом слове
        if char.isalpha():  # если символ буква то
            if char.isupper():  # мы смотрим заглавная буква это
                base = ord("A")  # запоминаем код буквы
                key_base = ord("A")  # переносим тот же код для ключа
            else:  # если строчные буквы
                base = ord("a")  # запоминаем код буквы с которой начинается
                # нужный алфавит
                key_base = ord("a")  # для ключа тоже
            shift = ord(keyword[keyword_index % len(keyword)]) - key_base
            # создаем переменную сдвиг, мы смотрим на текущий индекс символа в ключе,
            # делим его на длину ключа
            # так мы получаем букву, и ее код, а затем из кода при вычитании начала
            # алфавита получаем то на какую
            # длину надо переместь переменную
            shifted = (ord(char) - base + shift) % 26 + base  # переменная которая
            # получает код буквы для внесения в зашифрованный текст
            ciphertext += chr(shifted)  # добавляем букву под кодом шифтед
        else:  # если символ не буква
            ciphertext += char  # просто ее прибавляем к шифру
        keyword_index += 1  # и переходим к следующей букве в ключе
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
    plaintext = ""  # создаем пустую строку чтоюы записать туда дешифрованный текст
    keyword_index = 0  # индекс буквы которую мы рассматриваем в ключе
    for char in ciphertext:  # рассматриваем символы в простом слове
        if char.isalpha():  # если символ буква то
            if char.isupper():  # мы смотрим заглавная буква это
                base = ord("A")  # запоминаем код буквы
                key_base = ord("A")  # переносим тот же код для ключа
            else:  # если строчные буквы
                base = ord("a")  # запоминаем код буквы с которой начинается нужный алфавит
                key_base = ord("a")  # для ключа тоже
            shift = ord(keyword[keyword_index % len(keyword)]) - key_base
            # создаем переменную сдвиг, мы смотрим на текущий индекс символа в ключе, a
            # делим его на длину ключа так мы получаем букву, и ее код, а затем
            # из кода при вычитании начала алфавита получаем то на какую
            # длину надо переместь переменную
            shifted = (ord(char) - base - shift) % 26 + base  # переменная которая
            # получает код буквы для внесения в зашифрованный текст
            plaintext += chr(shifted)  # добавляем букву под кодом шифтед
        else:  # если символ не буква
            plaintext += char  # просто ее прибавляем к шифру
        keyword_index += 1  # и переходим к следующей букве в ключе
    return plaintext
