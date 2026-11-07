import random
import typing as tp


# создаем функцию для определения простое число или нет
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
    if n < 2:  # если число меньше двух(0, 1)
        return False
    for m in range(2, n):  # задаем переменную m, будем ее перебирать от 1 до n,
        # чтобы узнать при делении остается остаток или нет
        if n % m == 0:
            return False  # если не остается значит число непростое

    return True  # а если остается, то простое


def gcd(a: int, b: int) -> int:  # создаем функцию алгоритма Евклида,
    # чтобы найти НОД
    """
    Euclid's algorithm for determining the greatest common divisor.
    >>> gcd(12, 15)
    3
    >>> gcd(3, 7)
    1
    """
    if b == 0:  # если число б равно 0,
        return a  # то возвращаем просто число а
    return gcd(b, a % b)  # иначе мы возвращаем число а ставшее числом б,
    # и остаток от делеения а на б. повторяем функцию, уменьшаем число чтобы дойти до 0


def multiplicative_inverse(e: int, phi: int) -> int:  # создаем функцию
    # для расширенного алгоритма Евклида
    """
    Euclid's extended algorithm for finding the multiplicative
    inverse of two numbers.
    >>> multiplicative_inverse(7, 40)
    23
    """
    if phi == 1:  # обрабатываем граничный случай
        return 0  # по модулю 1 обратного не существует

    for d in range(1, phi):  # перебираем все числа от 1 до phi-1
        if (e * d) % phi == 1:  # проверяем условие: e * d mod phi = 1
            return d  # нашли обратное число

    return 0  # если не нашли, возвращаем 0


def generate_keypair(p: int, q: int) -> tp.Tuple[tp.Tuple[int, int], tp.Tuple[int, int]]:
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("Both numbers must be prime.")
    if p == q:
        raise ValueError("p and q cannot be equal")

    # n = pq
    n = p * q  #

    # phi = (p-1)(q-1)
    phi = (p - 1) * (q - 1)  #

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
