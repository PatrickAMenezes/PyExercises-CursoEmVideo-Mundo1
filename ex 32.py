def read_int(num):
    num = str(input(num))
    if num.isnumeric() == False:
        print('\033[1;31mERROR! Enter a valid integer.\033[m')
        print('-'*30)
        return False
    else:
        return num


print('-'*30)
n = read_int('Insert a number: ')
while n == False:
    n = read_int('Insert a number: ')
print(f'You just typed the number {n}.')
print('-'*30)
