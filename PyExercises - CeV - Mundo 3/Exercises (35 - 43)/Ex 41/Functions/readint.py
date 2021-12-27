def readint():
    while True:
        try:
            num = int(input('Insert a integer:'))
            if type(num) == int:
                return num
        except:
            print('\033[1;31mERROR: Please, insert a valid integer.\033[m')
