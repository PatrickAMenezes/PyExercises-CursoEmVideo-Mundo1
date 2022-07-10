num = int(input('Insert the quantity of terms to show: '))
a, b = 0, 1
n = 0
while n != num:
    print(a, end=' ')
    a, b = b, a + b
    n += 1
