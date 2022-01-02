from Functions.main.line import line
def menu():
    while True:
        try:
            print(line())
            print('\033[1;35mPeople Registration\033[m'.center(56))
            print(line())
            print('\033[1mSelect the option: ')
            print(line())
            for c in range(0, 3):
                if c == 0:
                    msg = 'Terminate Program'
                elif c == 1:
                    msg = 'Register person'
                else:
                    msg = 'List the registered people'
                print(f'\033[1;33m[{c}]\033[m \033[1;34m{msg}\033[m')
            print(line())
            option = int(input('\033[1mOption: '))
            print(line())
        except:
            print(line())
            print('\033[1;31mInvalid input.\033[m')
            continue
        else:
            return option
