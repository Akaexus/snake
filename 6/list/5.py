import random
a = []
for i in range(100):
    a.append(random.randint(0, 1000))

def _max(a):
    maxValue = a[0]
    for i in range(1, len(a)):
        if a[i] > maxValue:
            maxValue = a[i]
    return maxValue
print(_max(a))