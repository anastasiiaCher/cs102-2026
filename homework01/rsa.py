import random
import typing as tp


def is_prime(n: int) -> bool:
    """
    Tests to see if a number is prime.
    >>> is_prime(2)
    True
    >>> is_prime(11)
    True
    >>> is_prime(8)
    False
    """
    # PUT YOUR CODE HERE
    k = 2
    n_pr = True
    if n <= 1:
        n_pr = False
    else:
        while k**2 <= n:
            if n % k == 0:
                n_pr = False
                break
            k += 1
    return n_pr


def gcd(a: int, b: int) -> int:
    """
    Euclid's algorithm for determining the greatest common divisor.
    >>> gcd(12, 15)
    3
    >>> gcd(3, 7)
    1
    """
    # PUT YOUR CODE HERE
    if a == 0 and b == 0:
        return 0
    if a == 0 and b != 0:
        return b
    if a != 0 and b == 0:
        return a
    r = 1
    while r != 0:
        r = a % b
        if r != 0:
            a, b = b, r
    return b


def multiplicative_inverse(e: int, phi: int) -> int:
    """
    Euclid's extended algorithm for finding the multiplicative
    inverse of two numbers.
    >>> multiplicative_inverse(7, 40)
    23
    """
    # Сохраняем исходные значения phi и e
    const_phi = phi
    const_e = e

    # Меняем их, если нужно
    if e < phi:
        e, phi = phi, e

    r = 1
    div = []

    while r != 0:
        r = e % phi
        div.append(e // phi)  # 4-й столбец таблицы из учебника
        if r != 0:
            e, phi = phi, r

    # ПРОВЕРКА: если НОД != 1, обратного элемента нет
    # Поскольку ругается mypy, то предполагается, что такого не может быть
    # if phi != 1:
    #     return None

    x, y = 0, 1  # x, y из последней строки таблицы в учебнике

    # Обратный проход по столбцу с A//B
    for i in range(len(div) - 2, -1, -1):
        x, y = y, x - y * div[i]

    # Выбор правильной переменной и модуля
    if const_e < const_phi:
        answer = y % const_phi
    else:
        answer = x % const_phi
    return answer


def generate_keypair(p: int, q: int) -> tp.Tuple[tp.Tuple[int, int], tp.Tuple[int, int]]:
    """
    Генерация ключей
    """
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("Both numbers must be prime.")
    if p == q:
        raise ValueError("p and q cannot be equal")

    # n = pq
    # PUT YOUR CODE HERE
    n = p * q

    # phi = (p-1)(q-1)
    # PUT YOUR CODE HERE
    phi = (p - 1) * (q - 1)

    # Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)

    # Use Euclid's Algorithm to verify that e and phi(n) are coprime
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    # Use Extended Euclid's Algorithm to generate the private key
    d = multiplicative_inverse(e, phi)

    # Return public and private keypair
    # Public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n))


def encrypt(pk: tp.Tuple[int, int], plaintext: str) -> tp.List[int]:
    """
    Шифрование
    """
    # Unpack the key into it's components
    key, n = pk
    # Convert each letter in the plaintext to numbers based on
    # the character using a^b mod m
    cipher = [(ord(char) ** key) % n for char in plaintext]
    # Return the array of bytes
    return cipher


def decrypt(pk: tp.Tuple[int, int], ciphertext: tp.List[int]) -> str:
    """
    Расшифровка
    """
    # Unpack the key into its components
    key, n = pk
    # Generate the plaintext based on the ciphertext and key using a^b mod m
    plain = [chr((char**key) % n) for char in ciphertext]
    # Return the array of bytes as a string
    return "".join(plain)


if __name__ == "__main__":
    print("RSA Encrypter/ Decrypter")
    p = int(input("Enter a prime number (17, 19, 23, etc): "))
    q = int(input("Enter another prime number (Not one you entered above): "))
    print("Generating your public/private keypairs now . . .")
    public, private = generate_keypair(p, q)
    print("Your public key is ", public, " and your private key is ", private)
    message = input("Enter a message to encrypt with your private key: ")
    encrypted_msg = encrypt(private, message)
    print("Your encrypted message is: ")
    print("".join(map(lambda x: str(x), encrypted_msg)))
    print("Decrypting message with public key ", public, " . . .")
    print("Your message is:")
    print(decrypt(public, encrypted_msg))
