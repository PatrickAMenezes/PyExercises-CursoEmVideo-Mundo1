from random import randint
pc = randint(0, 10)
c = result = even_odd = 0
while True:
    print('='*54)
    num = int(input(('Insert a number from 0 to 10: ')))
    while num > 10:
        num = int(input(('Insert a number from 0 to 10: ')))
    option = str(input('Even or odd? [E/O]: ')).upper().strip()[0]
    while option not in 'EO':
        option = str(input('Even or odd? [E/O]: ')).upper().strip()[0]
    print('='*54)
    s = num + pc
    if s % 2 == 0:
        result = 'E'
        even_odd = 'even'
    elif s % 2 == 1:
        result = 'O'
        even_odd = 'odd'
    print(f'I choosed {pc} and you {num}. The total is {s}, gave {even_odd}.')
    if option == result:
        print('Congratulations!! You win, let\'s play again.')
        c += 1
    else:
        break
print(f'Game over!! Your consecutive win rate is {c}.')
print('-'*25, 'end', '-'*25)
