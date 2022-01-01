from Functions.line import line
def menu():
    while True:
        try:
            print(line())
            print('Select the option: ')
            print('[0] Terminate Program\n[1] Register person\n[2] List the registered people')
            print(line())
            option = int(input('Option: '))
            print(line())
            if option < 0 or option > 2:
                print('\033[1;31mPlease, insert a valid option.\033[m')
                continue 
        except:
            print('\033[1;31mPlease, insert a valid option.\033[m')
        else:
            break
    return option
