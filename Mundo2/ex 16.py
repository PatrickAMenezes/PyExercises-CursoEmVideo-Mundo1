count = 0
num = int(input('Insert a number: '))
for c in range (1, num + 1):
    if num % c == 0:
        count += 1
        print('\33[1;34m', end='')
    else:
        print('\33[1;31m', end='')
    print(c, end='  ')
print('\n\33[0mThe number {} is divisible {} times.'.format(num, count))
if count == 2:
    print('The number {} is prime.'.format(num))
else:
    print('The number {} is not prime.'.format(num))
