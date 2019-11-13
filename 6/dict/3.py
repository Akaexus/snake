words = {}
with open('pg28885.txt') as f:
    book = f.read().replace('.', '').replace('"', '').replace(',', '').split()
    for word in book:
        word = word.lower()
        if word not in words:
            words[word] = 1
        else:
            words[word] += 1
for word, count in sorted(words.items(), key=lambda x: x[0]):
    print('{}: {}'.format(word, count))