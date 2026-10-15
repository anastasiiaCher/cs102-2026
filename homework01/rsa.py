"""that actually was pretty fun to work on."""

import random
import typing as tp


def is_prime(n: int) -> bool:
    """a function i wrote like 2 years ago and still use.
    goes to sqrt(n) because this is the biggest divisor of n
    that exists if we look at min(k, n /k)
    (we search all the possible divisors by these pairs)
    p.s. wow yes very funny keep testing my function with negative numbers"""
    if n <= 1:
        return False

    for k in range(2, int((n**0.5) // 1 + 1)):
        if n % k == 0:
            return False

    return True


def gcd(a: int, b: int) -> int:
    """standard euclidian algorithm. not much to say"""
    while b != 0:
        a, b = b, a % b

    return a


def multiplicative_inverse(e: int, phi: int, x: int = 0, y: int = 1) -> int:
    """a rough version, yes. but it still works
    or just use pow(a, -1, b) like a normal person
    p.s. omg yes more edge cases please"""
    if e == 1 or phi == 1:
        return 0

    temp_list = []
    a, b = max(e, phi), min(e, phi)
    while b != 0:
        temp_list.append((a, b))
        a, b = b, a % b

    # print(temp_list)

    for i in range(len(temp_list) - 1):
        x, y = y, x - y * (temp_list[-i - 2][0] // temp_list[-i - 2][1])
        # print(x, y, temp_list[-i - 2][0] // temp_list[-i - 2][1])

    return y % max(temp_list[0])


def generate_keypair(
    p: int, q: int
) -> tp.Tuple[tp.Tuple[int, int], tp.Tuple[int, int]]:
    """the keypair generator. utilises every function we just wrote"""
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("Both numbers must be prime.")
    if p == q:
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
    """this function encrypts a line. who would have thought"""
    # Unpack the key into it's components
    key, n = pk
    # Convert each letter in the plaintext to numbers based on
    # the character using a^b mod m
    cipher = [(ord(char) ** key) % n for char in plaintext]
    # Return the array of bytes
    return cipher


def decrypt(pk: tp.Tuple[int, int], ciphertext: tp.List[int]) -> str:
    """this function decrypts a line. who would have thought"""
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
    # what is the reasoning behind using lambda here??
    print("Decrypting message with public key ", public, " . . .")
    print("Your message is:")
    print(decrypt(public, encrypted_msg))
