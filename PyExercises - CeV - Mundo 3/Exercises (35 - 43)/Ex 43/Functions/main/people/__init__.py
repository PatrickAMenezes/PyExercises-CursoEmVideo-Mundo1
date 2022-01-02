from Functions.main.line import line
def people():
    while True:
        try:
            qtt = int(input('\033[1mHow many people do you want to register?:\033[1m '))
        except:
            print('\033[1;31mInvalid input, insert a valid integer.\033[m')
        else:
            break
        print(line(), end='\n')
    return qtt
