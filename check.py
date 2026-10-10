
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
        if x not in "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm":
            ciphertext += x
        else:
            print(x)
            if x.isupper() == 1 and ord(x) + shift > 90:
                ciphertext += chr(ord(x) + shift - 26)
            elif x.isupper() == 1 and ord(x) + shift <= 90:
                ciphertext += chr(ord(x) + shift)
            if x.islower() == 1 and ord(x) + shift > 122:
                ciphertext += chr(ord(x) + shift - 26)
            elif x.islower() == 1 and ord(x) + shift <= 122:
                ciphertext += chr(ord(x) + shift)
            print(ciphertext)
    return ciphertext


str, shift = input("str: "), int(input("shift: "))
print(encrypt_caesar(str, shift))