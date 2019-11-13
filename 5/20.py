def remove_dups(astring):
    letters = []
    for letter in astring:
        if letter not in letters:
            letters.append(letter)
    return ''.join(letters)

print(remove_dups("mississippi"))   #should print misp

