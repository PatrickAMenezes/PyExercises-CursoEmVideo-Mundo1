def maior():
    print('-'*50)
    print('The numbers informed are: ', end='')
    for n in numbers:
        print(n, end= ' ')
    print('')
    print('-'*50)
    print(f'At all, were informed {len(numbers)} values.')
    print(f'The highest number informed was {max(numbers)}')
    print('-'*50)

def cont():
    c = str(input('Do you want to continue?[y/n]: ')).strip().lower()[0]
    while c not in 'yn':
        c = str(input('Do you want to continue?[y/n]: ')).strip().lower()[0]
    if c == 'y':
        numbers.clear()
    return c

numbers = []
while True:
    print('-'*50)
    quantity_num = int(input('How many numbers do you want to insert?: '))
    if quantity_num > 0:
        for q in range(quantity_num):
            num = int(input(f'Insert the {q+1}º number: '))
            numbers.append(num)
        maior()
    else:
        print('-'*50)
        print('There\'s no number informed.')
        print('-'*50)
    if cont() == 'n':
        break
print('-'*25 + '-'*25)
print(' '*20 + ' FINISHED ' + ' '*20)
print('-'*25 + '-'*25)
