def readfloat():
    while True:
        try:
            num = float(input('Insert a float: '))
            if type(num) == float:
                return num
        except:
            print('\033[1;31mERROR: Please, insert a valid float.\033[m')
