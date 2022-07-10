num = int(input('Insert a number: '))
print('The times table of {} is: '.format(num))
print('-'*18)
for c in range(1, 11):
    print('| {}  x {:>2} = {:>3} |'.format(num, c, num*c))
print('-'*18)
