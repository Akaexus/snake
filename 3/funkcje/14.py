def mySqrt(n):
    guess = n/2
    for i in range(1000):
        guess = 0.5 * (guess + (n/guess))
    return guess

print(mySquare(2))