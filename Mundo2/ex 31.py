while True:
    num = int(input('Insert a number: '))
    if num < 0:
        break
    print('-' * 13)
    for c in range (1, 11):
        print(f'{c} x {num} = {num * c}')
    print('-' * 13)
print('----- END -----')