num = list()
even = odd = 0
for c in range(0, 7):
    num.append(int(input('Insert a number: ')))
    if num[c] % 2 == 0:
        even += 1
    else:
        odd += 1
print('='*40)
# To see if there's even number or not.
if even >= 1:
    print(f'The even numbers are: ', end='')
else:
    print('There\'s no even number.', end='')
# If there's
for n in sorted(num):
    if n % 2 == 0:
        print(n, end=' ')
print('\n', end='')
# To see if there's odd number or not.
if odd >= 1:
    print('\nThe odd numbers are: ', end='')
else:
    print('There\'s no odd number.', end='')
# If there's
for n in sorted(num):
    if n % 2 == 1:
        print(n, end=' ')
print('\n', end='')
print('='*40)
