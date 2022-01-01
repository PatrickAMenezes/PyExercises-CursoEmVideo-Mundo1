from Functions.main.line import line
def menu():
    while True:
        try:
            print(line())
            print('\033[1;35mPeople Registration\033[m'.center(56))
            print(line())
            print('Select the option: ')
            print('\033[1;33m[0] Terminate Program\n[1] Register person\n[2] List the registered people\033[m')
            print(line())
            option = int(input('Option: '))
            print(line())
        except:
            print('\033[1;31mInvalid input.\033[m')
            continue
        else:
            return option
