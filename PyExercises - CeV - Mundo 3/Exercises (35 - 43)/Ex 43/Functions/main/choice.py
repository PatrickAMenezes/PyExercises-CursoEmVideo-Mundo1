from Functions.archieve import *
from Functions.main.menu import menu
def choice():
    while True:
        option = menu()
        if option == 0:
            print('\033[1;32mFinished!\033[m'.center(55))
            print(line())
            break
        elif option == 1:
            registration()
            continue
        elif option == 2:
            reading()
            continue 
        else:
            print('\033[1;31mPlease, insert a valid option.\033[m')
            menu()

