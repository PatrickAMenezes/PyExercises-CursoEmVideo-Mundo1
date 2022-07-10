numbers = list()
while True:
    num = int(input('Insert a number: '))
    numbers.append(num)
    cont = str(input('Do you want to continue? [y/n]: ')).lower().strip()[0]
    while cont not in 'yn':
        cont = str(input('Do you want to continue? [y/n]: ')).lower().strip()[0]
    if cont == 'n':
        break
print(f'You inserted a total of {len(numbers)} numbers.')
print(f'The numbers, in descending order, are: {sorted(numbers, reverse=True)}.')
if 5 in numbers:
    print(f'The number 5 appear {numbers.count(5)} times.')
else:
    print('The number 5 don\'t appear in the list.')
