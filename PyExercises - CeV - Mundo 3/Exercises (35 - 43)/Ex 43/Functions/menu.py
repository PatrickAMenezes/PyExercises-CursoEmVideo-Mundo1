def menu():
    while True:
        try:
            option = int(input('[0] Terminate Program / [1] Register people / [2] List the register people: '))
            if option < 0 or option > 2:
                print('\033[1;31mPlease, insert a valid option.\033[m')
                continue 
        except:
            print('\033[1;31mPlease, insert a valid option.\033[m')
        else:
            break
    return option
