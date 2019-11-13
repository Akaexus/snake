words = {}
with open('pg28885.txt') as f:
    book = f.read().replace('.', '').replace('"', '').replace(',', '').split()
    maxword = book[0]
    maxLen = 0
    for word in book:
        if len(word) > maxLen:
            maxword = word
            maxLen = len(word)
    print(maxword)
    print(maxLen)