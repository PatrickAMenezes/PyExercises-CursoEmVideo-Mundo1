def read_int(num):
    num = str(input(num))
    while True:
        # Analysing if the string is valid
        if num.isnumeric():
            break
        else:
            print('\033[1;31mERROR! Enter a valid integer.\033[m')
            print('-'*30)
            num = read_int('Insert a number: ')
    return num


print('-'*30)
n = read_int('Insert a number: ')
print(f'You typed the number {n}.')
print('-'*30)
