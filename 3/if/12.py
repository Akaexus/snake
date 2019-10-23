def isLeap(year):
    if year % 4:
        return False
    if not (year % 100):
        if year % 400:
            return False
    return True
