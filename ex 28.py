num = s = counter = 0
while num != 999:
    num = int(input('Insert a integer number until 999 (to stop type 999): '))
    s += num
    counter += 1
    if num > 999:
        s -= num
        counter -= 1
print('The quantity of numbers is {}.'.format(counter - 1), end=' ')
print('The sum between than is {}.'.format(s - 999))
