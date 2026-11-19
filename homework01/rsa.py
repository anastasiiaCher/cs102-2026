"""
1. Пользователь вводит два простых числа p и q
        │   (проверка: is_prime ✓)
        ▼
2. n = p · q                          ← войдёт в оба ключа
3. phi = (p − 1) · (q − 1)            ← секретное вспомогательное число
        │
        ▼
4. Выбираем случайное e: gcd(e, phi) = 1     (проверка: gcd ✓)
        │
        ▼
5. Находим d: (d · e) % phi == 1     (multiplicative_inverse ← сейчас)
        │
        ▼
открытый ключ (e, n)          закрытый ключ (d, n)


Шаг	Что делаем	Пример
1	берём два простых числа p и q	p = 3, q = 11
2	n = p · q	n = 33
3	phi = (p − 1) · (q − 1)	phi = 2 · 10 = 20
4	выбираем e, у которого с phi нет общих делителей	e = 7
5	находим d, такое что (d · e) % phi == 1	d = 3, ведь 21 % 20 = 1
"""

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
    if n < 2:  # маленькие числа
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:  # нашли делитель
            return False
    return True  # цикл закончился — делителей нет


def gcd(a: int, b: int) -> int:
    """
    Euclid's algorithm for determining the greatest common divisor.
    >>> gcd(12, 15)
    3
    >>> gcd(3, 7)
    1
    """
    while b > 0:
        a, b = b, a % b
    return a


# открытый (e, n)
# закрытый (d, n)


def multiplicative_inverse(e: int, phi: int) -> int:
    """
    Euclid's extended algorithm for finding the multiplicative
    inverse of two numbers.
    >>> multiplicative_inverse(7, 40)
    23
    """
    # multiplicative_inverse:
    a, b = phi, e  # цепочка Евклида начинается с phi и e
    x, y = 0, 1  # их счётчики: в phi 0 штук e, в e 1 штука e
    while b != 0:
        q = a // b  # сколько раз b помещается в a
        a, b = b, a % b  # (= a - q * b) шаг Евклида
        x, y = y, x - q * y  # тот же шаг со счётчиками
    return x % phi  # счётчик единицы, приведённый к нормальному виду


# на выходе d
# d подбирается так, чтобы (d · e) % phi == 1. Тогда расшифровка закрытым ключом возвращает исходное сообщение, зашифрованное открытым».


def generate_keypair(
    p: int, q: int
) -> tp.Tuple[tp.Tuple[int, int], tp.Tuple[int, int]]:
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("Both numbers must be prime.")
    elif p == q:
        raise ValueError("p and q cannot be equal")

    # n = pq
    n = p * q

    # phi = (p-1)(q-1)
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
    # Unpack the key into it's components
    key, n = pk
    # Convert each letter in the plaintext to numbers based on
    # the character using a^b mod m
    cipher = [(ord(char) ** key) % n for char in plaintext]
    # Return the array of bytes
    return cipher


def decrypt(pk: tp.Tuple[int, int], ciphertext: tp.List[int]) -> str:
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
    message = input("Enter a message to encrypt with your public key: ")
    encrypted_msg = encrypt(public, message)
    print("Your encrypted message is: ")
    print("".join(map(lambda x: str(x), encrypted_msg)))
    print("Decrypting message with private key ", public, " . . .")
    print("Your message is:")
    print(decrypt(private, encrypted_msg))
