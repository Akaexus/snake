size = 12

maxDigits = len(str(size**2))
printTemplate = '{0:'+str(maxDigits)+'}'

for i in range(1, size + 1):
    numbers = map(lambda n: printTemplate.format(n*i), range(1, size+1))
    print(' | '.join(numbers))

