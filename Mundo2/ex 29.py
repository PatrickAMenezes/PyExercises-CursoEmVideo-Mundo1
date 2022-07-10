s = cont = quantity = 0
bigger = smaller = 0
while cont != 'N':
    num = int(input('Insert a integer number: '))
    cont = str(input('Do you want to continue? [Y/N]: ')).upper().strip()[0]
    s += num
    quantity += 1
    while cont not in 'YN':
        cont = str(input('Please insert Y or N: ')).upper().strip()[0]
    if quantity == 1:
        bigger = smaller = num
    else:
        if num > bigger:
            bigger = num
        elif num < smaller:
            smaller = num
avg = s/quantity
print('-'*100)
print('You inserted a total of {} numbers which average is {}'.format(quantity, avg))
print('The sum between than is {}, the bigger is {} and the smaller is {}'.format(s, bigger, smaller))
print('-'*100)
