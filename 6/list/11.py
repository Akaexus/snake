def sumUntilEven(lst):
    s = 0
    for element in lst:
        if element % 2 == 0:
            break
        else:
            s += element
    return s
