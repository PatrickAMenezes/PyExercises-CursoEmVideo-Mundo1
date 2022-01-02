from Functions.main.line import line
from Functions.main.people import people
persons = {}
names = []
ages = []
def registration(file):
    qtt = people()
    if qtt >= 1:
        print(line())
        print('\033[1mRegistering...\033[m'.center(53))
        arch = open(f'{file}.txt', 'a')
    for i in range(qtt):
        print(line(), end='\n')
        while True:
            if i > 0 or (persons != {} and names == []):
                arch.write('\n')
            try:
                name = str(input('\033[1mName: ').strip().title())
                if name == '' or name.isnumeric() == True:
                    print('\033[1;31mInvalid name.\033[m')
                    continue
                else:
                    names.append(name)
                    break
            except:
                print('\033[1;31mInvalid input.\033[m')
        while True:
            try:
                age = int(input('\033[1mAge: '))
                if age < 0:
                    print('\033[1;31mInvalid age.\033[m')
                    continue
            except:
                print('\033[1;31mInvalid input.\033[m')
            else:
                ages.append(age)
                break
        print(line(), end = '\n')
        persons['names'] = names
        persons['ages'] = ages
        arch.write(f'{persons["names"][i]:<36}')
        arch.write(f'{persons["ages"][i]:>3} years')
        if i == (qtt-1):
            names.clear()
            ages.clear()
            arch.close()


def reading(file):
    try:
        arch = open(f'{file}.txt', 'r')
        print(line())
        print('\033[1mListing...\033[m'.center(53))
        print(line())
        print('\033[1m' + arch.read() + '\033[m')
        arch.close()
    except FileNotFoundError:
        print(line())
        print('\033[1mNon-existent file\033[m'.center(45))
        print(line())
