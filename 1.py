def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    ciphertext = ""
    # PUT YOUR CODE HERE
    for x in plaintext:
        if x not in "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm":
            ciphertext+=x
        else:
            if x.isupper ==  1 and ord(x)+shift  > 90:
                ciphertext+=chr(ord(x)+shift-26)
            elif x.isupper ==  1 and ord(x)+shift  <= 90:
                ciphertext+=chr(ord(x)+shift)
            if x.islower ==  1 and ord(x)+shift  > 90:
                ciphertext+=chr(ord(x)+shift-26)
            elif x.islower ==  1 and ord(x)+shift  <= 90:
                ciphertext+=chr(ord(x)+shift)

    return ciphertext

str,shift = input("str: "), int(input("shift: "))
print(encrypt_caesar(str,shift))