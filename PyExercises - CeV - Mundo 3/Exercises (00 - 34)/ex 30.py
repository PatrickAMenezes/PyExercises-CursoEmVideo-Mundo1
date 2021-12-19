def factorial(num, show=0):
    '''
    ------------------------------
    -> See the factorial of a num
    ------------------------------
    - num: Number to see the factorial;
    - f: Is the factorial of the number;
    - show: The user decides whether to see the factorial calculation or not.
    '''
    # Showing the factorial value
    f = 1
    for n in range(num, 0, -1):
        f *= n
    print('~'*54)
    print(f'The factorial of {num} is {f}')
    print('~'*54)
    # Asking if want to see the factorial calculation
    show = str(input('Do you want to see the factorial calculation?[y/n]: '))
    while show not in 'yn':
        show = str(input('Do you want to see the factorial calculation?[y/n]: '))
    # Showing the factorial calculation
    if show == 'y':
        for factorial in range(num, 0, -1):
            print(factorial, end = ' x ' if factorial > 1 else f' = {f}\n')
    print('~'*54)


print('~'*54)
num = int(input('Insert a number: '))
factorial(num)
