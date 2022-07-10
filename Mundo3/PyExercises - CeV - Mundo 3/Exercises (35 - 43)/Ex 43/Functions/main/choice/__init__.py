from Functions.archieve import *
from Functions.main.menu import menu
def choice():
    while True:
        option = menu()
        if option == 0:
            print('\033[1;32mFinished!\033[m'.center(55))
            print(line())
            break
        else:
            while True:
                try:
                    file = str(input('\033[1mInsert the file name: ')).strip()
                    print(line())
                    if file == '':
                        print('\033[1;31mInvalid file name.\033[m')
                        print(line())
                        continue
                except KeyboardInterrupt():
                    print('\033[1;31mInvalid input.\033[m')
                    print(line())
                else:
                    break
            try:
                if option == 1:
                    registration(file)
                    continue
                elif option == 2:
                    reading(file)
                    continue 
                else:
                    print('\033[1;31mPlease, insert a valid option.\033[m')
                    continue
            except:
                continue
