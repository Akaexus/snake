
def encrypt(cipherSet, message):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    cipher = {}
    for i in range(len(alphabet)):
        cipher[alphabet[i]] = cipherSet[i]
    return ''.join(map(lambda l: cipher[l], message))

print(encrypt('qwertyuiopasdfghjklzxcvbnm', 'dupa'))