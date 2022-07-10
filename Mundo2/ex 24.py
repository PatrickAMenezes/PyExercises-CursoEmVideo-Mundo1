# using while:
from math import factorial
num = int(input('Insert a number: '))
c1 = num
print('{}! = '.format(num), end= '')
while c1 != 0:
    print(c1, end='')
    print(' x ' if c1 > 1 else ' = ', end='')
    c1 -= 1
print(factorial(num))

# using for:
num2 = int(input('Insert a number: '))
print('{}! = '.format(num2), end='')
for c2 in range(num2, 0, -1):
    print('{} x '.format(c2) if c2 > 1 else '1 =', end='')
print('', factorial(num2))
