def sumEven(lst):
    lst = filter(lambda x: x % 2 == 0, lst)
    return sum(lst)

