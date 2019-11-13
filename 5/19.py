

def decrypt(cipherSet, message):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    cipher = {}
    for i in range(len(alphabet)):
        cipher[cipherSet[i]] = alphabet[i]
    return ''.join(map(lambda l: cipher[l], message))

print(decrypt('qwertyuiopasdfghjklzxcvbnm', 'rxhq'))