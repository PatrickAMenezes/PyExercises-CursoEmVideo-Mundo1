numbers = list()
num = apparitions = 0
n = 1
while True:
    num = int(input(f'{n}º value: '))
    n += 1
    if num not in numbers:
        numbers.append(num)
    else:
        print(f'This number ({num}) is alredy on the list.')
    cont = str(input('Do you want to continue [Y/N]: ')).upper().strip()[0]
    while cont not in 'YN':
        cont = str(input('Do you want to continue [Y/N]: ')).upper().strip()[0]
    if cont == 'N':
        break
print(f'The inserted numbers are: {sorted(numbers)}')
