from Functions.main.line import line
from Functions.main.people import people
def registration(file):
    qtt = people()
    if qtt >= 1:
        print(line())
        print('\033[1mRegistering...\033[m'.center(53))
    for i in range(qtt):
        arch = open(f'{file}.txt', 'a')
        arch.write(line())
        arch.write('\nName: ')
        print(line(), end='\n')
        while True:
            try:
                name = str(input('\033[1mName: ').strip().title())
                if name == '' or name.isalpha() == False:
                    print('\033[1;31mInvalid name.\033[m')
                    continue
                else:
                    arch.write(name + '\n')
                    break
            except:
                print('\033[1;31mInvalid input.\033[m')
        arch.write('Age: ')
        while True:
            try:
                age = int(input('\033[1mAge: '))
                if age < 0:
                    print('\033[1;31mInvalid age.\033[m')
                    continue
            except:
                print('\033[1;31mInvalid input.\033[m')
            else:
                arch.write(str(age) + '\n')
                break
        print(line(), end = '\n')
        arch.write(line() + '\n')
        if i == qtt:
            arch.close()


def reading(file):
    try:
        arch = open(f'{file}.txt', 'r')
        print(line())
        print('\033[1mListing...\033[m'.center(53))
        print('\033[1m', arch.read(), '\033[1m')
    except FileNotFoundError:
        print(line())
        print('\033[1mNon-existent file\033[m'.center(45))
        print(line())
