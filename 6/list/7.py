def countOdd(lst):
    lst = filter(lambda x: x % 2, lst)
    return len(lst)

