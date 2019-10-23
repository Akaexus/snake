year = int(input())
if not (1900 <= year <= 2099):
    print('date is out of range')
a = year % 19
b = year % 4
c = year % 7
d = (19 * a + 24) % 30
e = (2 * b + 4 * c + 6 * d + 5) % 7
dateofeaster = 22 + d + e
if year in [1954, 1981, 2049, 2076]:
    dateofeaster -= 7
if dateofeaster > 31:
    print('{} {}'.format('April', dateofeaster-31))
else:
    print('{} {}'.format('March', dateofeaster))
