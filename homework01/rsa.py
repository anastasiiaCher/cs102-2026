"""Simplified RSA encryption and decryption implementation."""

import random
import typing as tp


def is_prime(n: int) -> bool:
    """Check whether a number is prime.

    >>> is_prime(2)
    True
    >>> is_prime(11)
    True
    >>> is_prime(8)
    False
    """
    if n < 2:
        return False

    for divisor in range(2, int(n**0.5) + 1):
        if n % divisor == 0:
            return False

    return True


def gcd(a: int, b: int) -> int:
    """Find the greatest common divisor of two numbers.

    >>> gcd(12, 15)
    3
    >>> gcd(3, 7)
    1
    """
    while b != 0:
        a, b = b, a % b

    return a


def multiplicative_inverse(e: int, phi: int) -> int:
    """Find the multiplicative inverse of e modulo phi.

    >>> multiplicative_inverse(7, 40)
    23
    """
    old_r, remainder = e, phi
    old_s, coefficient = 1, 0

    while remainder != 0:
        quotient = old_r // remainder

        old_r, remainder = (
            remainder,
            old_r - quotient * remainder,
        )
        old_s, coefficient = (
            coefficient,
            old_s - quotient * coefficient,
        )

    return old_s % phi


def generate_keypair(
    p: int, q: int
) -> tp.Tuple[tp.Tuple[int, int], tp.Tuple[int, int]]:
    """Generate a public and private RSA key pair."""
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("Both numbers must be prime.")

    if p == q:
        raise ValueError("p and q cannot be equal")

    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randrange(1, phi)
    divisor = gcd(e, phi)

    while divisor != 1:
        e = random.randrange(1, phi)
        divisor = gcd(e, phi)

    d = multiplicative_inverse(e, phi)

    return ((e, n), (d, n))


def encrypt(pk: tp.Tuple[int, int], plaintext: str) -> tp.List[int]:
    """Encrypt plaintext using an RSA key."""
    key, n = pk
    return [pow(ord(char), key, n) for char in plaintext]


def decrypt(pk: tp.Tuple[int, int], ciphertext: tp.List[int]) -> str:
    """Decrypt ciphertext using an RSA key."""
    key, n = pk
    plain = [chr(pow(char, key, n)) for char in ciphertext]
    return "".join(plain)


if __name__ == "__main__":
    print("RSA Encrypter/ Decrypter")

    prime_p = int(input("Enter a prime number (17, 19, 23, etc): "))
    prime_q = int(input("Enter another prime number (Not one you entered above): "))

    print("Generating your public/private keypairs now . . .")

    public, private = generate_keypair(prime_p, prime_q)

    print(
        "Your public key is ",
        public,
        " and your private key is ",
        private,
    )

    message = input("Enter a message to encrypt with your private key: ")
    encrypted_msg = encrypt(private, message)

    print("Your encrypted message is: ")
    print("".join(map(str, encrypted_msg)))

    print("Decrypting message with public key ", public, " . . .")
    print("Your message is:")
    print(decrypt(public, encrypted_msg))
