def countWords(lst):
    return len(list(filter(lambda word: len(word) == 5, lst)))

print(countWords(['aaaaa']))