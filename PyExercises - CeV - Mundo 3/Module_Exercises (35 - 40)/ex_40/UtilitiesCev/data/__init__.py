def readmoney(msg):
    while True:
        inpt = str(input(msg)).strip()
        if ',' in inpt or '.' in inpt:
            break
        elif inpt.isnumeric() == False:
            print('ERROR: Invalid Value!')
        else:
            break
    res = inpt.replace(',', '.')
    return float(res)
