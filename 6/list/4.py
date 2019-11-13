import random
a = []
for i in range(100):
    a.append(random.randint(0, 1000))

def average(l):
    return sum(l)/len(l)
print(average(a))