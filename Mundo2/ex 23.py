n1 = float(input('Insert a number: '))
n2 = float(input('Insert another number: '))
if n1 > n2:
    greater = n1
elif n2 > n1:
    greater = n2
n5 = False
while not n5:
    question = int(input('Which process do you want to realize?\n[1] Sum\n'
    '[2] Multiplication\n[3] Show the greater\n[4] Input new numbers\n[5] Exit: '))
    if question == 5:
        n5 = True
    else:
        if question == 1:
            print('The sum between the 2 numbers is {}.'.format(n1 + n2))
        elif question == 2:
            print('The multiplication between the 2 numbers is {}.'.format(n1 * n2))
        elif question == 3:
            print('The greater between the 2 numbers is {}'.format(greater))
        elif question == 4:
            n1 = float(input('Insert a number: '))
            n2 = float(input('Insert another number: '))
        else:
            print('Invalid option.')
print('----- End -----')
