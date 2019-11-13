def count(elem, lst):
    c = 0
    for e in lst:
        if e == elem:
            c += 1
    return c

def _in(e, a):
    for element in a:
        if element == a:
            return True
    return False

def reverse(a):
    b = []
    for i in range(len(a)-1, -1, -1):
        b.append(a[i])
    return b

def index(e, a):
    for i in range(len(a)):
        if a[i] == e:
            return i
    return None

def insert(index, object, array):
    b = []
    for i in range(len(array)):
        if i == index:
            b.append(object)
        b.append(array[i])
    return b