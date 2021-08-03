from random import choices
lotery = list()
c1 = c2 = 0
while True:
    print('='*45)
    games = int(input('How many games do you want to play: '))
    print('='*45)
    while c1 != games:
        numbers = choices(range(0, 60), k = 6)
        lotery.append(numbers)
        c1 += 1
    print(f'Drawing {c1} games:')
    while c2 < len(lotery):
        print(f'Game {c2 + 1}: ', lotery[c2], end='')
        print()
        c2 += 1
    print('='*45)
    lotery.clear()
    c1 = 0
    c2 = 0
    cont = str(input('Do you want to show another games? [y/n]: ')).strip().lower()[0]
    while cont not in 'yn':
        cont = str (input('Do you want to show another games? [y/n]: ')).strip().lower()[0]
    if cont == 'n':
        break
print('='*45)
print(' '*17, 'Good Luck!')
print('='*45)
