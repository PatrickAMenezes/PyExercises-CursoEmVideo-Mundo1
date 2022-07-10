string = (str(input('Insert an expression: '))).strip()
ip = string.count('(')
fp = string.count(')')
if string.index(')') > string.index('('):
    if ip == fp:
        print('Your expression is correct.')
    else:
        print('Your expression is invalid.')
else:
    print('Your expression is invalid.')
