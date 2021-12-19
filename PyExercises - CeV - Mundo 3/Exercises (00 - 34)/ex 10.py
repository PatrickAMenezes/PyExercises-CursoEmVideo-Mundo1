numbers = list()
even = list()
odd = list()
while True:
    num = int(input('Insert a number: '))
    numbers.append(num)
    if num % 2 == 0:
        even.append(num)
    elif num % 2 == 1:
        odd.append(num)
    cont = str(input('Do you want to continue? [y/n]: ')).lower().strip()[0]
    while cont not in 'yn':
        cont = str(input('Do you want to continue? [y/n]: ')).lower().strip()[0]
    if cont == 'n':
        break
print(f'The entered numbers are: {sorted(numbers)}.')
print(f'The even numbers are: {sorted(even)}.')
print(f'The odd numbers are: {sorted(odd)}.')
