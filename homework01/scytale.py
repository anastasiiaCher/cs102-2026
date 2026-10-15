"""why are we here... just to suffer"""


def encrypt_scytale(n: int, plaintext: str) -> str:
    """
    >>> encrypt_scytale(4, 'НАС АТАКУЮТ')
    'НАУАТЮСАТ_К*'
    >>> scytale(5, 'этошифрдревнейспарты')
    'эфвптрнаодершрйтиесы'
    """
    ciphertext = ""

    """first we get the m, which is how many
    rows the table has. the amount of columns is n"""
    m = (len(plaintext) + n - 1) // n
    """then we make plaintext fit perfectly 
    into the table by adding asterisks
    and also replace the spaces with underscores,
    getting the perfect string."""
    plaintext += "*" * (m * n - len(plaintext))
    plaintext = plaintext.replace(" ", "_")
    # print(plaintext)

    mx_cipher = []

    for k in range(0, n * m, n):
        current_elem = list(plaintext[k : k + n])
        mx_cipher.append(current_elem)

    for i in range(n):
        for elem in mx_cipher:
            ciphertext += elem[i]

    return ciphertext
