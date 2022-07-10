sex = (input('Which is your sex [M/F]: ')).upper().strip()[0]
while sex not in 'MF':
        sex = str(input('Please insert a valid sex: ')).upper().strip()[0]
print('So your sex is {}, ok.'.format(sex))
