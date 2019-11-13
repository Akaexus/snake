s = input()
letters = {}

for letter in s:
    letter = letter.lower()
    if letter not in letters:
        letters[letter] = 1
    else:
        letters[letter] += 1

for key, value in sorted(letters.items(), key=lambda x: x[0]):
    print('{}: {}'.format(key, value))