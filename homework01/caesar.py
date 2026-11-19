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
    # PUT YOUR CODE HERE
    for char in plaintext:
        if char.isalpha(): # Проверяем, является ли символ буквой
            is_upper = char.isupper() # Запоминаем регистр (заглавная или строчная)
            char_code = ord(char.upper()) - 65 # Переводим букву в число от 0 до 25
            new_code = (char_code + shift) % 26 # Сдвигаем и берем остаток от деления на 26
            new_char = chr(new_code + 65) # Превращаем обратно в букву
            if not is_upper:
                new_char = new_char.lower() # Если буква была маленькой, делаем её маленькой
            ciphertext += new_char
        else:
            ciphertext += char # Если это не буква (цифра, пробел), оставляем как есть
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
    for char in ciphertext:
        if char.isalpha():
            is_upper = char.isupper()
            char_code = ord(char.upper()) - 65
            new_code = (char_code - shift) % 26 # Тут минус, так как мы расшифровываем
            new_char = chr(new_code + 65)
            if not is_upper:
                new_char = new_char.lower()
            plaintext += new_char
        else:
            plaintext += char
    return plaintext
