from Functions.main.line import line
from Functions.main.people import people
def registration():
    qtt = people()
    if qtt >= 1:
        print(line())
        print('Registering...'.center(44))
    for i in range(qtt):
        arch = open('teste.txt', 'a')
        arch.write(line())
        arch.write('\nName: ')
        print(line(), end='\n')
        while True:
            try:
                name = str(input('Name: ').strip().title())
                if name == '':
                    print('\033[1;31mInvalid name.\033[m')
                    continue
                else:
                    arch.write(name + '\n')
            except:
                print('\033[1;31mInvalid name.\033[m')
            else:
                break
        arch.write('Age: ')
        while True:
            try:
                age = int(input('Age: '))
                if age < 0:
                    print('\033[1;31mInvalid age.\033[m')
                    continue
            except:
                print('\033[1;31mInvalid age.\033[m')
            else:
                arch.write(str(age) + '\n')
                break
        print(line(), end = '\n')
        arch.write(line() + '\n')
        if i == qtt:
            arch.close()


def reading():
    try:
        arch = open('teste.txt', 'r')
        print(line())
        print('Listing...'.center(44))
        print(arch.read())
    except FileNotFoundError:
        print(line())
        print('Non-existent file'.center(45))
        print(line())
