"""
ciphertext = "Python3.6"
# PUT YOUR CODE HERE
tab = ""

tab = tab.maketrans(
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
    "DEFGHIJKLMNOPQRSTUVWXYZABCdefghijklmnopqrstuvwxyzabc"
)

print(ciphertext.translate(tab))

"""

tab=""
plaintext = "Sbwkrq3.2"
# PUT YOUR CODE HERE
tab = tab.maketrans(
    "DEFGHIJKLMNOPQRSTUVWXYZABCdefghijklmnopqrstuvwxyzabc",
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
)
print(plaintext.translate(tab))