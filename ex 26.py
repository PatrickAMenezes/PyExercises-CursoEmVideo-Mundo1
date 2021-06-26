first_term = int(input('Insert the first term of an Arithmetic Progression: '))
reason = int(input('Insert the reason of the arithmetic progression: '))
n = 0
end = False
while not end:
    ap = first_term + reason*n
    print(ap)
    if n < 9:
        n += 1
    else:
        end = str(input('Do you want to continue? [Y/N]: ')).upper().strip()[0]
        while end not in 'YN':
            end = False
            end = str(input('Please, insert Y or N: ')).upper().strip()[0]
        if end == 'N':
            end = True
        elif end == 'Y':
            end = False
            n += 1
print('----- END -----')
