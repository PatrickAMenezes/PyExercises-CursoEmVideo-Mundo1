def people():
    while True:
        try:
            qtt = int(input('How many people do you want to register?: '))
        except:
            print('\033[1;31mInvalid input, insert a valid integer.\033[m')
        else:
            break
    return qtt
