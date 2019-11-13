def count(substr,theStr):
    counter = 0
    newString = theStr
    while True:
        theStr = newString
        newString = theStr.replace(substr, '', 1)
        if newString == theStr:
            break
        else:
            counter += 1
    return counter