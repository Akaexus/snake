q = '''Assign to a variable in your program a triple-quoted string that contains your favorite paragraph of text -
perhaps a poem, a speech, instructions to bake a cake, some inspirational verses, etc.'''

def count(q):
    alphabet = {}
    for letter in q:
        l = letter.lower()
        if l not in alphabet:
            alphabet[l] = 1
        else:
            alphabet[l] += 1
    print("Your text contains {} alphabetic characters, of which {} ({}%) are 'e'.".format(
        len(q),
        alphabet['e'],
        round(alphabet['e']/len(q)*100, 1)
    ))
