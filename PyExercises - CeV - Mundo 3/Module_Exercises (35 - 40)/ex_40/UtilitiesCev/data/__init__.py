def readmoney(msg):
    while True:
        inpt = str(input(msg)).strip().replace(',', '.')
        if '.' in inpt or inpt.isnumeric() == True:
            return float(inpt)
        elif inpt.isnumeric() == False:
            print('\033[1;41mERROR: Invalid Value!\033[m')
